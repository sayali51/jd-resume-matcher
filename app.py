import os
import re
import PyPDF2
import spacy
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# ── Skill keywords database ───────────────────────────────────────────────────
SKILLS_DB = [
    "python", "java", "javascript", "c++", "c#", "r", "sql", "mysql",
    "postgresql", "mongodb", "flask", "django", "fastapi", "react", "nodejs",
    "html", "css", "machine learning", "deep learning", "nlp",
    "natural language processing", "computer vision", "tensorflow", "pytorch",
    "keras", "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn",
    "power bi", "tableau", "excel", "git", "github", "docker", "kubernetes",
    "aws", "azure", "gcp", "linux", "rest api", "data analysis",
    "data visualization", "statistical analysis", "hypothesis testing",
    "neural networks", "transformers", "bert", "opencv", "hadoop", "spark",
    "airflow", "etl", "data engineering", "feature engineering",
    "model deployment", "mlflow", "streamlit", "selenium", "web scraping",
    "communication", "teamwork", "problem solving", "leadership",
    "time management", "research", "agile", "scrum"
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_txt(file):
    return file.read().decode("utf-8", errors="ignore")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_skills(text):
    text_lower = text.lower()
    found = []
    for skill in SKILLS_DB:
        if skill.lower() in text_lower:
            found.append(skill)
    return list(set(found))

def get_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return round(float(score) * 100, 1)
    except:
        return 0.0

def get_verdict(score):
    if score >= 70:
        return "Strong Match", "green"
    elif score >= 45:
        return "Moderate Match", "orange"
    else:
        return "Weak Match", "red"

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get job description text
        jd_text = request.form.get('jd_text', '').strip()
        if not jd_text:
            return jsonify({'error': 'Please paste a job description.'}), 400

        # Get resume file
        resume_file = request.files.get('resume')
        if not resume_file:
            return jsonify({'error': 'Please upload a resume file.'}), 400

        filename = resume_file.filename.lower()
        if filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(resume_file)
        elif filename.endswith('.txt'):
            resume_text = extract_text_from_txt(resume_file)
        else:
            return jsonify({'error': 'Only PDF and TXT files supported.'}), 400

        if not resume_text.strip():
            return jsonify({'error': 'Could not extract text from resume.'}), 400

        # Clean texts
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)

        # Analysis
        score = get_match_score(clean_resume, clean_jd)
        verdict, color = get_verdict(score)

        resume_skills = extract_skills(clean_resume)
        jd_skills = extract_skills(clean_jd)

        matched_skills = [s for s in resume_skills if s in jd_skills]
        missing_skills = [s for s in jd_skills if s not in resume_skills]

        return jsonify({
            'score': score,
            'verdict': verdict,
            'verdict_color': color,
            'matched_skills': sorted(matched_skills),
            'missing_skills': sorted(missing_skills),
            'resume_skills_count': len(resume_skills),
            'jd_skills_count': len(jd_skills),
            'matched_count': len(matched_skills),
            'missing_count': len(missing_skills)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)