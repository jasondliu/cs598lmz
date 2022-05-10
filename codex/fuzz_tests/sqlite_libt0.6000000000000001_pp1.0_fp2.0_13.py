import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

from config import *
from utils import *
from db import *

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window")
        self.set_default_size(400, 200)
        self.connect("destroy", Gtk.main_quit)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.add(self.grid)

        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.props.title = "Window"
        self.set_titlebar(self.header)
        self.header.set_has_subtitle(False)

        self.btn_db = Gtk.Button()
        self.btn
