import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# import libraries
from PIL import ImageGrab
import os
import time
import win32api, win32con

# Globals
# ------------------

x_pad = 489
y_pad = 246

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    #'.png', 'PNG')
    return im

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOU
