import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('filename.db')
# Add the following line to your .bashrc file or wherever you want to add an alias (please change the path)
# alias dbus-send='python /path/to/dbus-send.py'

libc = ctypes.CDLL(ctypes.util.find_library('c'))

DBUS_NAME_FLAG_ALLOW_REPLACEMENT = 0x1
DBUS_NAME_FLAG_REPLACE_EXISTING = 0x2
DBUS_NAME_FLAG_DO_NOT_QUEUE = 0x4
DBUS_NAME_FLAG_ALLOW_REPLACEMENT = 0x1
DBUS_NAME_FLAG_REPLACE_EXISTING = 0x2
DBUS_NAME_FLAG_DO_NOT_QUEUE = 0x4
DBUS_NAME_FLAG_PROHIBIT_REPLACEMENT = 0x8
DBUS_NAME_FLAG_DO_NOT_QUEUE = 0x4
DBUS_NAME_FLAG_PROHIBIT_REPLACEMENT = 0x8
DBUS_
