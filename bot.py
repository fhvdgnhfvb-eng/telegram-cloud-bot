import telebot

TOKEN = "8513097794:AAFLHPCTAhLlz1A6bdE6nXqCJTiSWJzntZw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! Your bot is successfully running 😎")

@bot.message_handler(func=lambda message: True)
def echo(message):
    text = message.text
    processed = text.upper()  
    bot.reply_to(message, f"Processed text: {processed}")

print("Bot is running...")
bot.infinity_polling()