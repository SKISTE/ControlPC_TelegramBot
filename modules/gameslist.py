import os
from config import GAMES_DIR, check_lang_and_send


lang = check_lang_and_send()


def gameslist():
    temp = os.listdir(GAMES_DIR)
    text = ''
    for x in range(0, len(temp)):
        text = text + str(x + 1) + '. ' + temp[x][:-4] + '\n'
    del temp
    return text


def startgame(num):
    temp = os.listdir(GAMES_DIR)
    print(temp[int(num) - 1])
    text = f'{GAMES_DIR}/{temp[int(num) - 1]}'
    print(text)
    text = text.replace(' ', '^ ')
    os.system(text)
    return f'{lang.started} {temp[int(num) - 1][:-4]}'
