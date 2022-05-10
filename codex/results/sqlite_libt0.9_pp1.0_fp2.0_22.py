import ctypes
import ctypes.util
import threading
import sqlite3
import time

# This class is used to get the cdecl functions of both libsqlite3 and
# libpthread.  It's not a very elegant name, but get it?  Python sucks
# at this stuff.  At least with this I can change its name.
ctypes_func = ctypes.CDLL

# This is the name of the libpthread library on Linux... not much else
# I can say.
pthread_name = ctypes.util.find_library('pthread')

# Just set up the libpthread library for use with ctypes.
lpthread =  ctypes_func(pthread_name)

# This is the name of the libsqlite3 library on Linux... not much else
# I can say.
sqlite_name = ctypes.util.find_library('sqlite3')

# Just set up the libsqlite3 library for use with ctypes.
lsqlite3 = ctypes_func(sqlite_name)

# This is the name of the routines in libpthread we'll be using.  Once
# again in cdecl form
