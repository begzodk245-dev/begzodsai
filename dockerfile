FROM python:3.11-slim

WORKDIR /app

# Kerakli kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir pyTelegramBotAPI google-genai requests

# Kodlarimizni konteyner ichiga ko'chiramiz
COPY . .

# Bot faylini ishga tushiramiz
CMD ["python", "cloud_ai.py"]
