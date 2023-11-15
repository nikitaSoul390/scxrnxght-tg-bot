import telebot
from telebot import types

import citatnik_tg_bot
import photo_tg_bot

API_TOKEN = '6412153489:AAHAFkyy336TIXeqtCTXjN0mpLL39cy59wo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])

def start(message):

    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_citata = types.InlineKeyboardButton(text='Цитату давай🧐', callback_data='citata'); #кнопка «Да»
    keyboard.add(key_citata); #добавляем кнопку в клавиатуру
    key_pictire = types.InlineKeyboardButton(text='Картинку хочу😊', callback_data='pictire');  # кнопка «Да»
    keyboard.add(key_pictire);  # добавляем кнопку в клавиатуру
    key_phonk = types.InlineKeyboardButton(text='Фонка навали😈(Недоступно)', callback_data='phonk');  # кнопка «Да»
    keyboard.add(key_phonk);  # добавляем кнопку в клавиатуру
    question = ("Привет, как ты?😉\nЧто желаешь, смачную цитатку или прикольную картинку?🤔 Или же навалить лютого фонка?🥵😈🤙\nА также заходи сюда👉 @scxrnxght")
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "citata": #call.data это callback_data, которую мы указали при объявлении кнопки
        #код сохранения данных, или их обработки
        #bot.send_message(call.message.chat.id, 'Неважно кто ты по жизни, важно кто ты по поступкам! ☝️😈🤙')
        bot.send_message(call.message.chat.id, citatnik_tg_bot.random_citatnik())
    elif call.data == "pictire":
        #photo =  open(r'D:\Download\photo_5256006163542169775_y.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo_tg_bot.random_photo())
    elif call.data == "start":
        start()
    #elif call.data == "phonk":
       # audio = open(r'D:\Download\TOYOTENSHI - CAUSING HAVOC_(Mp3Bullet.ru).mp3', 'rb')
       # bot.send_audio(call.message.chat.id, audio)
      #  audio.close()

bot.polling(none_stop=True, interval=3)