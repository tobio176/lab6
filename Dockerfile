# Модель: Мікросервіс мережевої діагностики
# Автор: Тіторага Глєб, група АІ-233

FROM python:3.10-slim

WORKDIR /app

# Встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код
COPY main.py .

# Вказуємо порт
EXPOSE 5000

# Команда запуску
CMD ["python", "main.py"]