![CI](https://github.com/sayali51/jd-resume-matcher/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest&logoColor=white)

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
2. **Skill Gap Analysis** — keyword matching against a curated database of 60+ technical and soft skills

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| NLP | TF-IDF Vectorizer, spaCy |
| Similarity | Cosine Similarity (scikit-learn) |
| PDF Parsing | PyPDF2 |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Testing | Pytest |
| Deployment | Render (free tier) |

---

## Project Structure

```
jd-resume-matcher/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions — runs tests + Docker build on every push
│
├── tests/
│   ├── __init__.py
│   └── test_app.py             # Pytest suite — 3 automated tests
│
├── templates/
│   └── index.html              # Frontend UI — dark themed, responsive
│
├── static/                     # Static assets
├── app.py                      # Flask backend — routes, NLP logic, logging
├── Dockerfile                  # Container recipe
├── .dockerignore               # Docker build exclusions
├── requirements.txt            # Python dependencies
└── Procfile                    # Render deployment config
```

---

## Engineering Highlights

### Containerization (Docker)
The app is fully containerized. The Dockerfile uses layer caching — `requirements.txt` is copied and installed before the rest of the source code, so pip install only re-runs when dependencies change, not on every code change.

```bash
docker build -t jd-resume-matcher .
docker run -p 5000:5000 jd-resume-matcher
```

### CI/CD Pipeline (GitHub Actions)
Every push to `main` triggers a two-job pipeline in parallel:

| Job | What it does |
|-----|-------------|
| `test` | Installs dependencies, runs pytest suite on Ubuntu |
| `docker-build` | Builds the Docker image to verify containerization |

If either job fails, the push is flagged immediately — no broken code reaches the live deployment silently.

### Request Logging (Observability)
Every request and response is logged with timestamp, method, path, IP, status code, and duration:

```
2026-06-22 10:32:41 INFO → POST /analyze | IP: 192.168.1.1
2026-06-22 10:32:41 INFO ← 200 /analyze | 243ms
```

This uses Flask's `before_request` and `after_request` hooks with Python's `logging` module.

### Automated Tests (Pytest)
Three tests cover the critical paths:

| Test | What it verifies |
|------|-----------------|
| `test_home_loads` | Homepage returns HTTP 200 |
| `test_match_missing_fields` | `/analyze` handles empty input without crashing |
| `test_match_with_text` | Full analysis with a fake resume returns a valid score (0–100) |

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

## Run with Docker

```bash
# Build the image
docker build -t jd-resume-matcher .

# Run the container
docker run -p 5000:5000 jd-resume-matcher
```

Open browser at: `http://localhost:5000`

---

## Run Tests

```bash
python -m pytest tests/ -v
```

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

The matcher checks for 60+ skills across categories:

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

It directly extends my [AI Resume Parser](https://github.com/sayali51/AI-Resume-parser) project, adding the job-matching dimension. After building the core NLP logic, I retrofitted it with production engineering practices — Docker containerization, automated testing, and a CI/CD pipeline — to reflect how software is built and maintained professionally.

---

## Future Improvements

- [ ] Replace TF-IDF with sentence-transformer embeddings (BERT) for semantic similarity
- [ ] ATS keyword density scoring
- [ ] Resume section-wise analysis (Skills vs Experience vs Education)
- [ ] Suggest courses for missing skills
- [ ] Support for DOCX resume files
- [ ] Batch mode — match one resume against multiple JDs at once
- [ ] Push Docker image to Docker Hub automatically via CI

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
