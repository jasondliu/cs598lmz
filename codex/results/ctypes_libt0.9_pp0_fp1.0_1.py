import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello","alert", 0)
'''


# 1番 2番と振っていって、どちらが勝つかを当てるゲーム
from random import randint
import time, winsound
#from ctypes import *
from multiprocessing import Process, Queue
from multiprocessing.context import SpawnContext

'''
def beepMusic():
    winsound.Beep(float(440), 5000)
    time.sleep(0.0)
    winsound.Beep(float(600), 5000)
    time.sleep(0.0)
    winsound.Beep(float(400), 5000)
    time.sleep(0.0)
    winsound.Beep(float(800), 5000)
    time.sleep(0.0)
    winsound.Beep(float(300), 5000)
    time.sleep(0.0)
    winsound.Beep(float(100), 5000)
    time.sleep(0.0
