# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Скопируем файл с зависимостями (если он у вас называется requirements.txt)
COPY requirements.txt /app/

# Установим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем весь проект
COPY . /app/

# По умолчанию в docker-compose.yml мы переопределяем команду,
# так что CMD здесь можно оставить для отладки или пустым:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
