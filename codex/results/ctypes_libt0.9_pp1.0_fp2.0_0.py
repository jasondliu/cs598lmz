import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from Tkinter import * 
from sys import platform as _platform
if _platform == "win32":
    from Tkinter import Button
    from Tkinter import Tk
    import Tkinter as tk

#if _platform ==  "linux" or _platform == "linux2":
elif _platform == "darwin":
    from tkinter import * 
    from tkinter import Button
    from tkinter import Tk
    import tkinter as tk

root = Tk()

root.geometry("1870x945+0+0")


def buttonClose():
    root.quit()
    root.destroy()   

def openFile():
    import os
    #from ctypes import windll  
    from PIL import Image

    #if _platform == "win32":
    if _platform == "darwin":
        pass
        #windll.shcore.SetProcessDpiAwareness(1)

    import ttk
    import tk
