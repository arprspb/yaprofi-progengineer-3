from python:3.10-slim-buster
workdir /app
copy requirements.txt .
run pip install -r requirements.txt
copy . .
cmd uvicorn main:app --host 0.0.0.0 --port 5000 --reload