import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

# "Official" C-types
c_word = ctypes.c_uint16
c_dword = ctypes.c_uint32
c_qword = ctypes.c_uint64
c_time64 = c_qword

# Python 2.6 doesn't have a c_ssize_t in the standard ctypes library
c_ssize_t = getattr(ctypes, 'c_ssize_t', ctypes.c_int)

_dbus_bindings = ctypes.CDLL(ctypes.util.find_library('dbus-1'))

# DBusWatchFlags
DBUS_WATCH_READABLE = 0x01
DBUS_WATCH_WRITABLE = 0x02
DBUS_WATCH_ERROR = 0x04
DBUS_WATCH_HANGUP = 0x08

# DBusSignalFlags
DBUS_SIGNAL_FLAG_NO_MATCH_RULE = 1
DBUS_SIGNAL_FLAG_MATCH_ARG0_NAMESPACE = 2
DBUS_SIGNAL
