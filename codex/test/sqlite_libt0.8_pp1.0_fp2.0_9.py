import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import datetime
import platform

# Suppress version check warning
# It's annoying.
def suppress_urwid_warning():
    import urwid
    urwid.set_encoding("UTF-8")
    urwid.VERSION = (1, 3, 1)

suppress_urwid_warning()

