import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter as tk
from tkinter import messagebox
messagebox.showinfo("Title", "a Tk MessageBox")

from tkinter import *
from tkinter import messagebox

root = Tk()
def callback():
    if messagebox.askyesno('Verify', 'Really quit?'):
        messagebox.showwarning('Yes', 'Not yet implemented')
    else:
        messagebox.showinfo('No', 'Quit has been cancelled')

Button(root, text='Quit', command=callback).pack(fill=X)
Button(root, text='Spam', command=(lambda:
        messagebox.showinfo('Spam', 'Spam Selected'))).pack(fill=X)
root.mainloop()

from tkinter import *
from tkinter import messagebox

root = Tk()

def callback():
    if messagebox.askyesno('Verify', 'Really quit?'):
        messagebox.showwarning('
