# Base image
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential curl

# Copy requirements from root (now in context)
COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy app source code
COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
