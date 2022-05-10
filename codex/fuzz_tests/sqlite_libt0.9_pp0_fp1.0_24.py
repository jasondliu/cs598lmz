import ctypes
import ctypes.util
import threading
import sqlite3
import platform
import subprocess
import os


debug = False

try:
    import settings
except Exception as e:
    print e
    print "please copy settings.py.example to setting.py and configure CONFIG_DB_FILE, LOOKUPSERVER_PASSWORD and LOOKUPSERVER_PORT"
    print ""
    print "EXITING"
    os._exit(1)


try:
    settings.CONFIG_DB_FILE, settings.LOOKUPSERVER_PASSWORD, settings.LOOKUPSERVER_PORT
except Exception as e:
    print e
    print "please copy settings.py.example to setting.py and configure CONFIG_DB_FILE, LOOKUPSERVER_PASSWORD and LOOKUPSERVER_PORT"
    print ""
    print "EXITING"
    os._exit(1)


class LookupServer():
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
        self.libc.setproctitle
