FROM python:3.10-slim

# Evita prompts de tzdata y reduce capa
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Solo deps primero (cache mejor)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia código
COPY app.py .
# El modelo se copiará en CI *después* de entrenar:
# COPY model/creditcard-v1.joblib model/creditcard-v1.joblib

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
