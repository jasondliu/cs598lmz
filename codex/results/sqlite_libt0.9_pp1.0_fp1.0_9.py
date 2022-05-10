import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import re
import os

appName = "App Inventor"
appPrefs = appName + " Preferences"
appProfile = appName + " Profile"

import urllib
import urllib2
import HTMLParser

TEMPLATE = "%Y-%m-%d %H:%M:%S"

# Python 2.x and 3.x difference
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

if os.name == "nt":
    debug = False
else:
    debug = False

# ID of the last record in the database
# so that we don't have to read it twice
# last_record_id = None

# is the key being pressed?
key_is_pressed = False

# mutex so that we don't spam the database
# and to verify that the key is not being pressed
mutex = threading.Lock()

# do we have a new key?
new_key = False

# List of key_ids of the current key press
key_ids =
