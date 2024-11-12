# Use uma imagem base oficial do Python
FROM python:3.12.6-alpine

# Crie um diretório de trabalho
WORKDIR /app

COPY . .

RUN python -m pip install redis

CMD ["python", "redis-flush.py"]