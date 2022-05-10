import ctypes
ctypes.windll.user32.MessageBoxW(0, "This is a message", "", 1)
import os
import tkinter
from tkinter import *

def testFunction():
    print('Button Clicked')

root = Tk()
root.title('Test Title')
root.geometry('917x917')

myButton = Button(master=root, text="Click Me", command=testFunction)
myButton.grid(row=0, column=0)

root.mainloop()

# Test 1
import os
import tkinter
from tkinter import *

def testFunction():
    print('Button Clicked')

root = Tk()
root.title('Test Title')
root.geometry('917x917')

myButton = Button(master=root, text="Click Me", command=testFunction)
myButton.grid(row=0, column=0)

root.mainloop()

# Test 2
import os
import tkinter
from tkinter import *

def testFunction():
    print('Button Click
