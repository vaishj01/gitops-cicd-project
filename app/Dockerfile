# 1. Base image: a lightweight Linux with Python 3.12 already installed
FROM python:3.12-slim

# 2. Python settings: don't write .pyc files, print logs immediately
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. All commands run from the /app folder inside the container
WORKDIR /app

# 4. Copy requirements first and install them (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Then copy the app code (tests are NOT copied - not needed in production)
COPY main.py .

# 6. Security: don't run as root, use a normal user
RUN useradd --create-home appuser
USER appuser

# 7. Document which port the app listens on
EXPOSE 8000

# 8. Command that starts when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]