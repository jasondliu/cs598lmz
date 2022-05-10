import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import Tkinter
import ttk
import tkMessageBox
import tkFileDialog

import sys
import os
import csv
import shutil
import datetime
import re
import copy

#------------------------------------------------------------------------------

def main():
    """Main function"""

    root = Tkinter.Tk()
    root.title("Anki Deck Generator")

    # preserve the selected directory and file across sessions
    try:
        with open("settings.txt") as f:
            settings = f.read()
            directory = settings.split("\n")[0]
            filepath = settings.split("\n")[1]
    except IOError:
        directory = ""
        filepath = ""

    app = Application(root, directory, filepath)
    app.mainloop()

def update_settings(directory, filepath):
    """Preserve the selected directory and file across sessions"""

    with open("settings.txt", "w") as f:
       
