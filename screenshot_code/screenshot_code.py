import pyautogui
import time


def screenshot():
    time.sleep(3)
    img=pyautogui.screenshot('screenshot.png')
    img.show('the image is here')


if __name__== "__main__":
    screenshot()
