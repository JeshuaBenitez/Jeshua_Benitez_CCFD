# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# 1) Instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 2) Copiar app y modelo entrenado
COPY app.py .
COPY model/ model/

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
