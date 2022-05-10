import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
# Test sqlite3.connect()

# Test sqlite3.Connection.execute()
cursor.execute("select 42")
result = next(cursor)
# Test sqlite3.Connection.execute()

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class App(object):
    def __init__(self):
        window = Gtk.Window()
        window.set_title("Test")
        window.connect("destroy", Gtk.main_quit)
        button = Gtk.Button("hello")
        button.connect("clicked", self.on_hello_clicked)
        window.add(button)
        window.show_all()

    def on_hello_clicked(self, button):
        pass

App()
Gtk.main()

import PyQt5.Qt
Qt.QApplication([])

import sys
sys
# import tests.test
