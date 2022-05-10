import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import sys
import time

# This is a simple script to periodically poll the database and send
# a notification when a new item is added to the database.
#
# The script can be triggered by running 'python push.py' from the
# command line.
#
# The script requires the following packages:
#
# - PyObjC (http://pyobjc.sourceforge.net/)
# - libnotify (http://developer.gnome.org/libnotify/)

# This is the path to the database.
#
# If you're running the script on the same machine as the server,
# this is probably fine.
#
# If you're running the script on a different machine, you'll need
# to change this.
DB_PATH = './db/db.sqlite3'

# This is the path to the server's log file.
#
# If you're running the script on the same machine as the server,
# this is probably fine.
#
# If you're running the script on a different machine, you'll need
# to change this.

