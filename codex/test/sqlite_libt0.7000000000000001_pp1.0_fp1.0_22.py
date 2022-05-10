import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import time
import threading
import re
import shutil
import Queue
import threading
import sys
import math
import hashlib

if getattr(sys, 'frozen', False):
    # we are running in a |PyInstaller| bundle
    basedir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    basedir = os.path.dirname(__file__)

#stdout_write = sys.stdout.write
#stderr_write = sys.stderr.write
#sys.stdout.write = lambda x: stdout_write(x)
#sys.stderr.write = lambda x: stderr_write(x)

#sys.stdout = open(basedir+"/debug.txt", "w", buffering=0)
#sys.stderr = sys.stdout

#print "basedir: " + basedir

# We assume the executable is in the same directory as the database
