import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
import time
import sys
import getopt

# The following is a hack to support both Python2 and Python3
# Python3 renamed raw_input to input
try:
    input = raw_input
except NameError:
    pass


# The following is a hack to support both Python2 and Python3
# Python3 renamed urllib2 to urllib.request
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

# The following is a hack to support both Python2 and Python3
# Python3 renamed Tkinter to tkinter
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

# The following is a hack to support both Python2 and Python3
# Python3 renamed tkMessageBox to messagebox
try:
    import tkMessageBox
except ImportError:
    from tkinter import messagebox


# Global variables

# The default location of the database file
