import codecs
codecs.register_error('strict', codecs.ignore_errors)

import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.scrolledtext as tkst
import tkinter.filedialog as tkfd
import tkinter.font as tkf

import json


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Twitch Chat Replay")

        self.resizable(False, False)
        self.option_add("*font", "Sans 11")

        self.top_bar = tk.Frame(self)
        self.top_bar.pack(side="top", fill="x")

        self.settings_file = tk.StringVar(self.top_bar)
        self.settings_file.set(os.path.join(os.path.dirname(__file__), "settings.json"))

        self.settings_file_entry = tk.Entry(self.top
