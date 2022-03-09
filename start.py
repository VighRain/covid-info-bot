import telebot

token = '5234059386:AAFWTu3CFmu_HjAx1yTq0qGxlhQHe2EqEyA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(m, res=False):
        with open('info.txt', encoding="utf-8") as f:
                info = f.read()
        bot.send_message(m.chat.id, info)

@bot.message_handler(content_types=['text'])
def handle_text(message):
	bot.send_message(message.chat.id, 'Message received: ' + message.text)

bot.infinity_polling()
