TOKEN = ''
ALLOWED_IDS = ['']
GAMES_DIR = ''

import language


def check_lang_and_send():
    settings = open('settings.txt', 'r', encoding='utf-8').read().split('=')
    if settings[1] == 'ru':
        return language.RU()
    elif settings[1] == 'en':
        return language.EN()
