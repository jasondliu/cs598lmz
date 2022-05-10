import ctypes
ctypes.windll.user32.SetProcessDPIAware()
from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter.ttk import Separator
import subprocess
import sys
from tkinter.ttk import Combobox as CBox
from tkinter import scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk
import shutil
import time


class MainMenu:
    """
    Main Menu Class
    """
    def __init__(self, master, images_path):
        """
        Constructor
        :param master: Tk
        :param images_path: String
        """
        self.master = master
        self.images_path = images_path
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.configure(background="white")
        self
