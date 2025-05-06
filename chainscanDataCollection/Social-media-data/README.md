# Social-media-data

Create virtual environment: mkdir social_analysis
cd social_analysis
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install fastapi[all]  # Install FastAPI with optional dependencies

Testing:  curl -X POST "http://127.0.0.1:8000/analyze" -H "Content-Type: application/json" -d '{"username": "john_doe", "content": "I love FastAPI! This is amazing."}'
