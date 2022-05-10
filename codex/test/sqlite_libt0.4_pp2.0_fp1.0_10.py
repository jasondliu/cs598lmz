import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

from ctypes import *

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf

import pygame
from pygame.locals import *

#----------------------------------------------------------------------------------

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Bomber")
        self.set_default_size(600, 600)
        self.set_border_width(10)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('Default Page!'))
        self.notebook.append_page(self.page1, Gtk.Label('Page 1'))

        self.page2 = Gtk.Box()
