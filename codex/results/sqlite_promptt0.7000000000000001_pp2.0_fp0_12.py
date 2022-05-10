import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') for sqlite3 in memory option
from time import sleep
import sys
# from getch import getch

if sys.version_info.major == 2:
    # running under python 2.7
    from Tkinter import *
    import Tkinter as tk
else:
    # running under python 3.x
    from tkinter import *
    import tkinter as tk

from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.commondialog import *
from tkinter.scrolledtext import *

def build_db_from_csv(path):
    #db = sqlite3.connect(':memory:')
    db = sqlite3.connect(path)
    cur = db.cursor()

    cur.execute("DROP TABLE IF EXISTS dictionary")
    sql_cmd = """CREATE TABLE dictionary (
    id INTEGER PRIMARY KEY,
    word TEXT
