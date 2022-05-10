import sys, threading

def run():
    import ctypes
    ctypes.windll.shell32.IsUserAnAdmin()
    #import os, sys
    #cmd = 'pip install requests'
    #os.system(cmd)
    #print(os.system(cmd))
    #os.system('cmd /k "pip install requests"')
    #os.system(sys.executable + ' -m pip install -U pip')
    #os.system(sys.executable + ' -m pip install requests')
    #os.system(sys.executable + ' -m pip install pypiwin32')

def run2():
    import os
    os.system('pip install requests')
    os.system('pip install pypiwin32')

t = threading.Thread(target=run)
t.start()

#t2 = threading.Thread(target=run2)
#t2.start()

from tkinter import *

root = Tk()

root.geometry('500x500')
root.title('test')

#text = Text(
