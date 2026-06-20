# 🎯 JD Resume Matcher

**Live Demo → [https://jd-resume-matcher-261h.onrender.com](https://jd-resume-matcher-261h.onrender.com)**

> ⚠️ Hosted on Render free tier — may take 30–60 seconds to wake up on first visit.

---

## What It Does

Paste any job description and upload your resume — the system instantly tells you:

- 📊 **Match Score** — percentage compatibility between your resume and the JD
- ✅ **Skills You Have** — skills from the JD already present in your resume
- ❌ **Skills You're Missing** — gaps you need to address before applying
- 💡 **Smart Verdict** — Strong / Moderate / Weak match with actionable advice

---

## How It Works

```
Job Description Text
        +                  →  TF-IDF Vectorization  →  Cosine Similarity  →  Match Score %
Resume Text (PDF/TXT)

                           →  Skill Keyword Extraction  →  Matched / Missing Skills
```

**Two-layer analysis:**

1. **Semantic Similarity** — TF-IDF vectorizes both texts, cosine similarity measures overall content overlap
2. **Skill Gap Analysis** — keyword matching against a curated database of 50+ technical and soft skills

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| NLP | spaCy, TF-IDF Vectorizer |
| Similarity | Cosine Similarity (scikit-learn) |
| PDF Parsing | PyPDF2 |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Deployment | Render (free tier) |

---

## Project Structure

```
jd-resume-matcher/
│
├── app.py                  # Flask app — routes, NLP logic, skill extraction
├── requirements.txt        # Python dependencies
├── Procfile                # Render deployment config
│
├── templates/
│   └── index.html          # Frontend UI — dark themed, responsive
│
└── static/                 # Static assets
```

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/sayali51/jd-resume-matcher.git
cd jd-resume-matcher

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 4. Run the app
python app.py
```

Open browser at: `http://127.0.0.1:5000`

---

## Sample Output

```
Job Description: Data Analyst role requiring Python, SQL, Power BI, Excel

Resume Uploaded: Sayali_Kale_Resume.pdf

Match Score:     72.4%
Verdict:         Strong Match ✅

Skills You Have:    python, excel, communication, data analysis
Skills Missing:     sql, power bi

💡 Strong match! Tailor your resume summary to mirror the JD language and apply confidently.
```

---

## Skills Database

The matcher checks for 50+ skills across categories:

| Category | Skills Covered |
|----------|---------------|
| Programming | Python, Java, JavaScript, C++, R, SQL |
| ML & AI | Machine Learning, Deep Learning, NLP, TensorFlow, PyTorch, scikit-learn |
| Data | Pandas, NumPy, Excel, Power BI, Tableau, ETL |
| Web | Flask, Django, React, HTML, CSS, REST API |
| Cloud & DevOps | AWS, Azure, GCP, Docker, Kubernetes |
| Soft Skills | Communication, Leadership, Teamwork, Problem Solving |

---

## Why I Built This

While applying for internships, I noticed that manually comparing job descriptions to my resume was time-consuming and inconsistent. This tool automates that process — giving a data-driven answer to "should I apply for this role?" and "what should I add to my resume first?"

It directly extends my [AI Resume Parser](https://github.com/sayali51/AI-Resume-parser) project, adding the job-matching dimension.

---

## Future Improvements

- [ ] ATS keyword density scoring
- [ ] Resume section-wise analysis (Skills vs Experience vs Education)
- [ ] Suggest courses for missing skills
- [ ] Support for DOCX resume files
- [ ] Batch mode — match one resume against multiple JDs at once

---

## Related Project

**AI Resume Parser** — upload a resume, get category prediction + skill extraction + job recommendation
- Live: [https://ai-resume-parser-9mo4.onrender.com](https://ai-resume-parser-9mo4.onrender.com)
- Code: [github.com/sayali51/AI-Resume-parser](https://github.com/sayali51/AI-Resume-parser)

---

## Author

**Sayali Kale**
- 📧 sayalikale364@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/sayali-kale-42001a2b1)
- 💻 [GitHub](https://github.com/sayali51)
- 📍 Pune, India

---

## License

This project is open source and available under the [MIT License](LICENSE).
