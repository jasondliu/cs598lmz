import ctypes
ctypes.windll.user32.MessageBoxW(0, "Error. Please check the fields", "Error", 1)

# --------------------------

# To allow the user to choose a file

from tkinter import filedialog

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

# --------------------------

# To allow the user to choose a directory

from tkinter import filedialog

root = Tk()
root.directory = filedialog.askdirectory()
print (root.directory)

# --------------------------

# To switch between frames in tkinter

import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(
