import ctypes
import ctypes.util
import threading
import sqlite3

import sys
import time
import subprocess
import os

try:
    from gi.repository import GObject, Gtk
except ImportError:
    import gobject as GObject
    import gtk as Gtk

try:
    gtk_version = Gtk.get_major_version()
    text_buffer = Gtk.TextBuffer
    text_iter = Gtk.TextIter
    text_mark = Gtk.TextMark
    MenuItem = Gtk.MenuItem
    menu_get_active = Gtk.Menu.get_active
except AttributeError:
    gtk_version = 2
    text_buffer = Gtk.TextBuffer
    text_iter = Gtk.TextIter
    text_mark = Gtk.TextMark
    MenuItem = Gtk.MenuItem
    menu_get_active = Gtk.Menu.get_active

try:
    from gi.repository import GLib, GObject, Gtk, Gdk
except ImportError:
    import gobject as GObject
    import gtk as Gtk
