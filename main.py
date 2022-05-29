from config import *
import telebot
from time import sleep
from modules import *
import traceback
import os
import language
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

settings = open('settings.txt', 'r', encoding='utf-8').read().split('=')
if settings[1] == 'ru':
    lang = language.RU()
elif settings[1] == 'en':
    lang = language.EN()
print(settings[1])

bot = telebot.TeleBot(TOKEN)


def checkId(id):
    if str(id) in ALLOWED_IDS:
        return True
    else:
        return False


def gen_markup(row: int, buttons: dict):
    markup = InlineKeyboardMarkup()
    markup.row_width = row
    for x in buttons.keys():
        markup.add(InlineKeyboardButton(x, callback_data=buttons[x]))
    return markup


@bot.message_handler(commands=["help",'помощь'])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, lang.help)
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["volume",'громкость'])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, lang.change_volume,
                             reply_markup=gen_markup(3, {'▲': 'vol_up', '▼': 'vol_down', '%': 'vol_perc'}))
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["nexttrack",'след'])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, nexttrack())
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["prevtrack"])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, prevtrack())
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["pause"])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, pause())
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["ping"])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, lang.pong)
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["shutdown"])
def command(message):
    try:
        if checkId(message.chat.id):
            temp, delay = message.text.split(' ')
            if delay != '0':
                os.system(f'shutdown /s /t {str(int(delay) * 60)}')
                bot.send_message(message.chat.id, f'{pc_shutdown}{str(delay)} {minute}')
            else:
                os.system('shutdown /a')
                bot.send_message(message.chat.id, lang.remove_pc_shutdown)
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["screen"])
def command(message):
    try:
        if checkId(message.chat.id):
            temp = screenshot()
            bot.send_photo(message.chat.id, temp)
            temp.close()
            os.remove('screen.png')
    except Exception as e:
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["games"])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, gameslist())
    except Exception as e:
        traceback.print_exc()
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


@bot.message_handler(commands=["start"])
def command(message):
    try:
        if checkId(message.chat.id):
            bot.send_message(message.chat.id, startgame(message.text.split(' ')[1]))
    except Exception as e:
        traceback.print_exc()
        bot.send_message(message.chat.id, f'{lang.error}\n{str(e)}')


#
# EVENT LISTENER
#
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "vol_up":
        volup()
        bot.answer_callback_query(call.id, lang.volume + get_current_volume())
    elif call.data == "vol_down":
        voldown()
        bot.answer_callback_query(call.id, lang.volume + get_current_volume())
    elif call.data == 'vol_perc':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=lang.change_volume_percent,
                              reply_markup=gen_markup(10,
                                                      {'0%': 'vol_0', '10%': 'vol_10', '20%': 'vol_20', '30%': 'vol_30',
                                                       '40%': 'vol_40', '50%': 'vol_50', '60%': 'vol_60',
                                                       '70%': 'vol_70', '80%': 'vol_80', '90%': 'vol_90',
                                                       '100%': 'vol_100'}))
    elif call.data == 'vol_0':
        volume(0)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}0%')
    elif call.data == 'vol_10':
        volume(10)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}10%')
    elif call.data == 'vol_20':
        volume(20)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}20%')
    elif call.data == 'vol_30':
        volume(30)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}30%')
    elif call.data == 'vol_40':
        volume(40)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}40%')
    elif call.data == 'vol_50':
        volume(50)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}50%')
    elif call.data == 'vol_60':
        volume(60)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}60%')
    elif call.data == 'vol_70':
        volume(70)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}70%')
    elif call.data == 'vol_80':
        volume(80)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}80%')
    elif call.data == 'vol_90':
        volume(90)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}90%')
    elif call.data == 'vol_100':
        volume(100)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{lang.volume_set}100%')


# Запускаем бота
bot.polling(none_stop=True, interval=0)
