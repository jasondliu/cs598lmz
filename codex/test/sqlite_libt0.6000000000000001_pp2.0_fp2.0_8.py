import ctypes
import ctypes.util
import threading
import sqlite3
import time
import locale
import sys
import os
import random

# set locale to unicode
locale.setlocale(locale.LC_ALL, '')

# get libc
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# open up the db
conn = sqlite3.connect('movies.db')
c = conn.cursor()

# set the tty to raw mode
libc.tcgetattr(0, ctypes.byref(old_tty))
new_tty = old_tty
new_tty.c_lflag &= ~(termios.ICANON | termios.ECHO)
libc.tcsetattr(0, termios.TCSANOW, ctypes.byref(new_tty))

# set up the curses window
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def get_movies(genre=None):
    """Get a list of movies"""
