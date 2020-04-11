# -*- coding:utf-8 -*-

import time
from PIL import ImageGrab
from pynput.keyboard import Key, Controller, Listener
from ctypes import windll


user32 = windll.user32
user32.SetProcessDPIAware()

def help_manual():
    print('\n\nScreenshots are stored at place where this application is present.')
    print('\nSimply hit left-shift and screen shot will be saved.\n\n')

def welcome():
    
    print("""
'  _________                                   \n /   _____/ ___________   ____   ____   ____  \n \\_____  \\_/ ___\\_  __ \\_/ __ \\_/ __ \\ /    \\ \n /        \\  \\___|  | \\/\\  ___/\\  ___/|   |  \\\n/_______  /\\___  >__|    \\___  >\\___  >___|  /\n        \\/     \\/            \\/     \\/     \\/ \n  ________            ___.                 \n /  _____/___________ \\_ |__   ___________ \n/   \\  __\\_  __ \\__  \\ | __ \\_/ __ \\_  __ \\\n\\    \\_\\  \\  | \\// __ \\| \\_\\ \\  ___/|  | \\/\n \\______  /__|  (____  /___  /\\___  >__|   \n        \\/           \\/    \\/     \\/       \n'

""")
    print('\n-Kush')

welcome()
help_manual()

count=1
def count_update():
    global count
    print('Screenshots Grabbed: '+str(count), end='\r')
    count+=1

def grab_show():
    im=ImageGrab.grab(bbox=None)
    im.save(str(time.time()) + '.jpg')

def on_press(key):
    pass

def on_release(key):
        if key == Key.shift :
            grab_show()
            count_update()
            
keyboard = Controller()

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

