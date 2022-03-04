import telebot
import config
from telebot import types
import random
from telebot import REPLY_MARKUP_TYPES

# Создаем экземпляр бота
bot = telebot.TeleBot(config.TOKEN)
responsible_list = ['Аня', 'Лена', 'Никита', 'Мурат', 'Дима', 'Володя']


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Назначить ответственных")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Добро пожаловать, я бот "Охотник 1.0". Создан для определения ответственных лиц',
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["stop"])
def stop(message, res=False):
    bot.send_message(message.chat.id, "Бот отключен")
    if message.text == "stop":
        bot.stop_bot()


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Назначить ответственных':
        bot.send_message(message.chat.id, 'Ответственные:')
        a = bot.send_message(message.chat.id, str(random.sample(responsible_list, 2)))
    # else:
    #     bot.send_message(message.chat.id, 'Не понимаю вас. Я запрограммирован отвечать на запрос :'
    #                                       ' "Назначить ответственных"')


# Запускаем бота
bot.polling(none_stop=True, interval=0)
