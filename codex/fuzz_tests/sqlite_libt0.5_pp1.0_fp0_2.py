import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os

# Linux
if sys.platform == 'linux':
    from ctypes.util import find_library
    libc = ctypes.CDLL(find_library('c'))
# Mac OS X
elif sys.platform == 'darwin':
    libc = ctypes.CDLL('libc.dylib')
# Windows
else:
    libc = ctypes.CDLL('msvcrt')

libc.setlocale(ctypes.LC_ALL, '')

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Lan Messenger")
        self.set_default_size(600, 400)
        self.set_border_width(10)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.chat_
