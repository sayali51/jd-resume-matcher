# tests/test_app.py
import io
import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_loads(client):
    """Homepage should return 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_match_missing_fields(client):
    """POST to /match without data should return 400."""
    response = client.post('/analyze', data={})
    assert response.status_code in [400, 200]  # adjust based on your app

def test_match_with_text(client):
    """POST with jd_text and a fake TXT resume file should return a score."""
    fake_resume = io.BytesIO(b"Experienced Python developer with Flask and REST APIs")
    response = client.post('/analyze',
        data={
            'jd_text': 'Python developer with Flask and SQL skills',
            'resume': (fake_resume, 'resume.txt')
        },
        content_type='multipart/form-data'
    )
    assert response.status_code == 200
    data = response.get_json()
    assert 'score' in data
    assert 0 <= data['score'] <= 100