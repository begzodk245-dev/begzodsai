import telebot
from google import genai

# Siz taqdim etgan mutlaqo aniq va xatolarsiz Telegram hamda Google API kalitlari
TELEGRAM_TOKEN = "9108334219:AAG_luuzpkFd9zJQ52DpjfxXFj3fCEIKRSs"
API_KEY = "AIzaSyDav70ZrKZcmf2eJwI7edrPV9rH-Ng_E7I"

# Bot va Gemini mijozlarini ishga tushiramiz
bot = telebot.TeleBot(TELEGRAM_TOKEN)
gemini_client = genai.Client(api_key=API_KEY)

# Foydalanuvchi /start yoki /help buyrug'ini yuborganida
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Salom! Men Google Gemini (eng yangi gemini-3.8-flash) sun'iy intellekti asosida ishlaydigan botman.🤖\n\n"
        "Menga istalgan savolingizni bering, sizga o'zbek tilida javob qaytaraman!"
    )
    bot.reply_to(message, welcome_text)

# Foydalanuvchidan kelgan har qanday matnli xabarni qayta ishlash
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_question = message.text
    
    # Bot foydalanuvchiga javob o'ylayotganini ko'rsatishi uchun (Typing status)
    bot.send_chat_action(message.chat.id, 'typing')
    
    try:
        # Gemini modeliga foydalanuvchi savolini yuboramiz
        response = gemini_client.models.generate_content(
            model='gemini-3.8-flash',
            contents=user_question,
        )
        ai_response = response.text
        
        # Sun'iy intellekt javobini foydalanuvchiga yuboramiz
        bot.reply_to(message, ai_response, parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi, iltimos qayta urinib ko'ring.\nBatafsil: {str(e)}")

if __name__ == "__main__":
    print("Bot muvaffaqiyatli ishga tushdi... Telegram'ga kirib xabar yozishingiz mumkin!")
    # Botni tinimsiz ishlash rejimiga o'tkazamiz
    bot.infinity_polling()
