FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.5.1

WORKDIR /app

# Install system deps
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libffi-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "2"]
