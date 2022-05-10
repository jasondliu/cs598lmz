import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re

# this is a hack to find the correct path to the libnotify so file
# it is needed since we use py2exe to generate the executable
# this hack is better than the previous one, but still needs a
# bit of cleaning up
_libnotify_path = ctypes.util.find_library('notify')
if not _libnotify_path:
    if sys.platform[:3] == 'win':
        _libnotify_path = os.path.normpath(os.path.join(
            os.path.dirname(sys.argv[0]), 'notify.dll'))
    else:
        _libnotify_path = os.path.normpath(os.path.join(
            os.path.dirname(sys.argv[0]), '../lib/libnotify.so'))
libnotify = ctypes.CDLL(_libnotify_path)

# we need to keep a reference to the callbacks we added
# to prevent them from getting garbage collected
_reminders =
