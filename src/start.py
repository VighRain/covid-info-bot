"""Основной скрипт для работы бота"""
import telebot

token = '5234059386:AAFWTu3CFmu_HjAx1yTq0qGxlhQHe2EqEyA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	"""Вывод на экран начального меню бота"""
	with open('../data/start.txt', encoding="utf-8") as f:
		start = f.read()
	markup = telebot.types.InlineKeyboardMarkup()
	info_button = markup.add(telebot.types.InlineKeyboardButton(text='Инфо', callback_data=1))
	stats_button = markup.add(telebot.types.InlineKeyboardButton(text='Статистика', callback_data=2))
	tourism_button = markup.add(telebot.types.InlineKeyboardButton(text='Туризм', callback_data=3))
	health_button = markup.add(telebot.types.InlineKeyboardButton(text='Медицинская помощь', callback_data=4))
	bot.send_message(message.chat.id, text=start, reply_markup=markup)
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
	bot.send_message(message.chat.id, 'Message received: ' + message.text)

if __name__ == '__main__':
        bot.infinity_polling()
