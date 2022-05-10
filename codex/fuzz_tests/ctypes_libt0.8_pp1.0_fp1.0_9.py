import ctypes
ctypes.windll.user32.ShowWindow(x, 0)

import tkinter
from tkinter import *
import tkinter.ttk as ttk
import os
import sys

def create_window():
    window = Tk()
    window.title("Auto Clicker")
    window.geometry('350x350')
    
    from datetime import date
    from tkcalendar import Calendar, DateEntry
    from tkinter import messagebox
    from PIL import Image, ImageTk
    import datetime
    import time
    import subprocess
    import threading
    import ctypes
    import keyboard
    import tkinter as tk

    class App(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)
            self.title("Auto Clicker")
            self.geometry('350x350')
            self.resizable(0,0)
            
            # Info text
            self.info = Label(window, text="Press Alt+F4 to exit the program", fg="black", font=
