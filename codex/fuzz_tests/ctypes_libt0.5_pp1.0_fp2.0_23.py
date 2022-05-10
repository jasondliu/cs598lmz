import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time
import pyautogui

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Application(Frame):
    """ GUI Application for the simple calculator. """

    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.create_widgets2()

    def create_widgets(self):
        """ Create widgets to get user input and display output. """
        # create label to get
