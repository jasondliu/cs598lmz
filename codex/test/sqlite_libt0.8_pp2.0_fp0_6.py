import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import hashlib
import datetime
import sys
import os
import platform

pyperclip.copy("Test")
pyperclip.paste()

# SQLite database setup
conn = sqlite3.connect('snippets.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS snippets (title text, keywords text, text text)')
conn.commit()
conn.close()

# Key press listener setup
user32 = ctypes.windll.user32
user32.keybd_event(0x12, 0, 0, 0)
user32.keybd_event(0x12, 0, 0x0002, 0)

# https://gist.github.com/chriskiehl/2906125
def on_press(key):
    # Keys to ignore
    ignore = ['Key.cmd', 'Key.alt_l', 'Key.alt_r', 'Key.caps_lock', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.shift', 'Key.shift_r']

    #
