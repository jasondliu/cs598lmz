import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import uuid

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

# Set up logging
import logging
logging.basicConfig(filename='/tmp/latch-gnome.log', level=logging.DEBUG)

# Set up the sqlite database
if not os.path.isfile(os.getenv("HOME")+"/.latch-gnome/latch.db"):
    os.makedirs(os.getenv("HOME")+"/.latch-gnome/")
    conn = sqlite3.connect(os.getenv("HOME")+"/.latch-gnome/latch.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE LATCH_APP_ID (appid text)''')
    c.execute('''CREATE TABLE LATCH_SECRET (secret text)''')
