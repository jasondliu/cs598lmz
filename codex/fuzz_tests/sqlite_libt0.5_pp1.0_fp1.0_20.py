import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import re

# Create a new thread to handle the UI
class UI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("MPD Client")
        self.root.geometry("200x200")
        self.root.resizable(0,0)

        # Create a label that will display the current song
        self.label = tk.Label(self.root, text="Current Song:")
        self.label.pack()

        # Create a label that will display the current song
        self.song_label = tk.Label(self.root, text="")
        self.song_label.pack()

        # Create a label that will display the
