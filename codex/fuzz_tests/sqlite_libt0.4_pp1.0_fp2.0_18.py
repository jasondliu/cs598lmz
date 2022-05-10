import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import subprocess
import signal
import traceback

import pygtk
pygtk.require('2.0')
import gtk
import gobject

import config
import db
import utils
import widgets
import ui

import dbus
import dbus.service
import dbus.mainloop.glib

# Check for new pynotify
if gtk.pynotify.is_initted():
    gtk.pynotify.uninit()
gtk.pynotify.init("Pithos")

# Check for new appindicator
if hasattr(gtk.status_icon_position_menu, '__call__'):
    gtk.status_icon.position_menu = gtk.status_icon_position_menu

class PithosWindow(gtk.Window):
    __gsignals__ = {
        'show-hide-toggle': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
    }
    def __init__(
