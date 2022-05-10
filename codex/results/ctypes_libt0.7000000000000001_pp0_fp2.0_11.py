import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

from tkinter import Tk
from tkinter.messagebox import showinfo

def show():
    showinfo("Title", "a Tk MessageBox")

root = Tk()
root.after(5000, show)
root.mainloop()
