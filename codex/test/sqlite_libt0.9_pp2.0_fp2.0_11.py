import ctypes
import ctypes.util
import threading
import sqlite3
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta

from .cui import CUI
from .gui import GUI
from . import logtool

from .defaults import *
from . import defaults


def open_browser(*x):
    webbrowser.open('https://open.spotify.com/')


class Core:

    def __init__(self):

        # Helper classes
        self.time = Time()
        self.io = IOHandler()
        self.pulse = Pulse()
        self.i18n = I18n('./l10n/ro.json', self)
        self.py_to_c = CSafe()
        self.discogs = Discogs()

        self.show_countdown = False

        # Module init
        self.log = logtool.Logger(self, __name__)

        # UI
        self.cui = CUI(self)
