import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# This is a hack to find the location of the libdbus-1.so library.
# TODO: Find a better way to do this.
libdbus_path = ctypes.util.find_library("dbus-1")
libdbus = ctypes.CDLL(libdbus_path)

# C types
c_bool = ctypes.c_bool
c_char = ctypes.c_char
c_char_p = ctypes.c_char_p
c_double = ctypes.c_double
c_int = ctypes.c_int
c_long = ctypes.c_long
c_short = ctypes.c_short
c_uint = ctypes.c_uint
c_ulong = ctypes.c_ulong
c_ushort = ctypes.c_ushort
c_void_p = ctypes.c_void_p

# DBus types
dbus_bool = c_bool
dbus_int32 = c_int
dbus_uint32 = c_uint
dbus_
