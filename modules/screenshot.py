import pyautogui


def screenshot():
    img = pyautogui.screenshot('screen.png')
    img = open('screen.png', 'rb')
    return img
