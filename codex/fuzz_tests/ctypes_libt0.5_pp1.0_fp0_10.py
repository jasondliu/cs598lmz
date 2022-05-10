import ctypes
ctypes.windll.user32.SetProcessDPIAware()
#from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
import subprocess
import sys
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

class mainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Slicer")
        self.geometry("600x450+50+50")
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.iconbitmap(self.resource_path('icon.ico'))
        self.bind('<Return>', self.on_enter)
        self.bind('<Escape>', self.exit_app)
        self.createWidgets()

    def resource_path(self, relative_path):
        """ Get absolute path to
