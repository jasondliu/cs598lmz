import ctypes
import ctypes.util
import threading
import sqlite3
import sqlite3.dbapi2 as lite
import os
import time

from gi.repository import Gtk, Gdk, GObject, GLib, Notify

def _(message) :
	return message

