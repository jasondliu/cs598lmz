import ctypes
import ctypes.util
import threading
import sqlite3
import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib

import sys
sys.path.append('../')
import wnck

# https://github.com/amoffat/pbs
import pbs


class WindowLogger(threading.Thread):
    def __init__(self):
        super(WindowLogger, self).__init__()
        self.__quit = threading.Event()
        self.__window_change =  threading.Event()
        self.__window = None


    def run(self):
        f = open('window.log', 'w')
        while not self.__quit.is_set():
            self.__window_change.clear()
            f.write( u"{}\n".format(self.__window) )
            f.flush()
            self.__window_change.wait()
        f.close()


    @
