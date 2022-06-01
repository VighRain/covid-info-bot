"""Основной скрипт для работы бота"""
import telebot
from bot_token import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
        """
        Вывод на экран начального меню бота.

        Выводится приветствие из /data/start.txt
        и отображаются 5 кнопок для взаимодействия с ботом.
        
        """
        with open('../data/start.txt', encoding="utf-8") as f:
                start = f.read()
        markup = telebot.types.InlineKeyboardMarkup()
        info_button = markup.add(telebot.types.InlineKeyboardButton(text='Инфо', callback_data=1))
        stats_button = markup.add(telebot.types.InlineKeyboardButton(text='Статистика', callback_data=2))
        tourism_button = markup.add(telebot.types.InlineKeyboardButton(text='Туризм', callback_data=3))
        health_button = markup.add(telebot.types.InlineKeyboardButton(text='Медицинская помощь', callback_data=4))
        bot.send_message(message.chat.id, text=start, reply_markup=markup)
        
@bot.message_handler(commands=['info'])
def info(message):
        """
        Ввывод общей информации о вирусе и эпидемии.
        
        Выводится из /data/info.txt
        
        """
        with open('../data/info.txt', encoding="utf-8") as f:
                info = f.read()
        bot.send_message(message.chat.id, text=info)

@bot.message_handler(commands=['stats'])
def stats(message):
        """
        Показ статистики по выбранной стране.

        """
        bot.send_message(message.chat.id, "hi")


@bot.message_handler(commands=['tourism'])
def tourism(message):
        """
        Показ ограничений на перемещение
        в выбранной стране

        """
        pass


@bot.message_handler(commands=['health'])
def health(message):
        """
        Показ номеров горячих линий
        или учереждение здравоохранения
        в выбранной стране

        """
        pass


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
        """
        Обработчик меню.

        Получает callback_data из нажатой кнопки
        и выполняет соответствующее кнопки действие.
        
        """

        bot.answer_callback_query(callback_query_id=call.id)
        
        if call.data == '1':
                info(call.message)
        elif call.data == '2':
                stats(call.message)
        elif call.data == '3':
                tourism(call.message)
        elif call.data == '4':
                health(call.message)

def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://covid-info-bot-tele.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == '__main__':
        bot.infinity_polling()
