from PIL import ImageGrab
from pyperclip import paste
from datetime import datetime
from random import choice
from string import ascii_letters


class ClipToImg:
    @classmethod
    def img_to_file(cls):
        filename = f"{datetime.today().strftime('%m-%d-%H_%M')}-{''.join(choice(ascii_letters) for i in range(3))}.png"
        ImageGrab.grabclipboard().save(filename)
        print(f"Image saved into {filename}")

    @classmethod
    def start(cls):
        if paste() != "":
            print("Clipboard contains text!")
        elif ImageGrab.grabclipboard() != None:
            cls.img_to_file()
        else:
            print("Clipboard empty!")


def run():
    ClipToImg.start()
