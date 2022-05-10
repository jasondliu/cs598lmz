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

def log(str):
    print datetime.datetime.now(), str

# Monkey-patching ctypes makes it look for libraries in other places
# than the default, e.g.:
#
# ctypes.util.find_library('spotify')
#
# which would normally try searching for "libspotify.*" on system paths and
# return None.  patch_find_library() makes it additionally look
# for "spotify.*" in the current working directory and then the name
# as-is.  (The latter is not really necessary here, but can be useful
# when dealing with proprietary libraries that aren't prefixed with 'lib'.)
#
# This allows us to simply distribute the libspotify library with the
# application instead of requiring the
