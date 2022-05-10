import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import os
import shutil
import sys
import time
import datetime
import threading
import subprocess
import logging
import re

# from tkinter.ttk import *

class TkinterGUI(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initLogging()
        self.initDirectory()
        self.initVariable()
        self.initOptionMenu()
        self.initText()
        self.initButton()
        self.initProgressBar()
        self.initImage()
        self.initTreeview()

    def initUI(self):
        self.parent.title("Image Renamer")
        self.parent.geometry("900x600")
