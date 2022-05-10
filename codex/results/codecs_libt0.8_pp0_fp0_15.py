import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)                                                                                                   # support for utf-8 for Windows

# imports for the application
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import os.path


class MainWindow:
    def __init__(self, parent):
        # initialize main window
        self.main_window = tk.Toplevel(parent)
        self.main_window.title('WorkFlowTool')
        self.main_window.geometry('1200x768')
        self.main_window.iconbitmap('icon.ico')
        self.main_window.grid_columnconfigure(0, weight=1)
        self.main_window.grid_columnconfigure(1, weight=1)
        self.main_window.grid_rowconfigure(0, weight=1)

        # add textfield for project name
        self.project_name_label = ttk.Label(self.main_window, text='
