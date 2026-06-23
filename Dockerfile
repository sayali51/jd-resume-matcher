FROM python:3.12-slim

WORKDIR /app

# System deps needed to build some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first — caches this layer so rebuilds are fast
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Now copy the rest of the app
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]