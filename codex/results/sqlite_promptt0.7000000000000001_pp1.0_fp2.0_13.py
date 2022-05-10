import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() first in case it's not available.
sqlite3.connect('test.db')

import logging
logging.basicConfig(level=logging.DEBUG)

from gi.repository import Gtk, GtkSource, GObject, Gdk, GdkPixbuf, Pango

#--------------------------------------------------------------------
# Main window
#--------------------------------------------------------------------

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Lilypond Snippets")

        self.set_default_size(750, 400)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.add(self.scrolled_window)

        self.treeview = Gtk.TreeView()
        self.treeview.set_headers_visible(False)
        self.treeview.connect('button-press-event', self.button_press_event)
        self.treeview.connect('button-release-event', self.button_release_event)
        self.treeview.connect('key-press-
