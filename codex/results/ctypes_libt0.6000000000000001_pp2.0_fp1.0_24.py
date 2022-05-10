import ctypes
ctypes.windll.user32.MessageBoxW(0, 'Your text', 'Your title', 1)

# https://stackoverflow.com/questions/14254902/how-to-display-a-message-box-in-python
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Your text', 'Your title', 0)

# https://stackoverflow.com/questions/14254902/how-to-display-a-message-box-in-python
from Tkinter import *
import tkMessageBox

tkMessageBox.showinfo("Title", "a Tk MessageBox")

root = Tk()
root.withdraw()
tkMessageBox.showinfo("Title", "a Tk MessageBox")

# https://stackoverflow.com/questions/14254902/how-to-display-a-message-box-in-python
from Tkinter import *
import tkMessageBox

root = Tk()
root.withdraw()
tkMessageBox.showinfo("
