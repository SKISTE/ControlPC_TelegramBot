import pyautogui
from config import check_lang_and_send


lang = check_lang_and_send()

def nexttrack():
    pyautogui.press('nexttrack')
    return lang.nexttrack


def prevtrack():
    pyautogui.press('prevtrack')
    return lang.nexttrack


def pause():
    pyautogui.press('playpause')
    return lang.pausemusic
