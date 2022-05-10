import lzma
lzma.__version__

import sys
print(sys.version)
print(sys.version_info)

#%%

import tkinter
tkinter._test()

#%%

'''
import turtle
turtle.fd(100)
turtle.done()
'''

''' ERROR!
from turtle import *
fd(100)
done()
'''

#%%

from math import sqrt
print("sqrt(81) =", sqrt(81))

#%%

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()

#%%

from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('E
