import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(:memory:)
import os
import re
import socket
import sys
import time
import unittest
import warnings
import weakref

# Skip test if sqlite library cannot be found.
sqlite = ctypes.util.find_library('sqlite3')
if sqlite is None:
    raise unittest.SkipTest('sqlite3 not available')

# Skip test if sqlite library does not have the required version.
version = sys.version_info[:2]
if version == (2, 6):
    required_sqlite = '3.6.0'
elif version == (2, 7):
    required_sqlite = '3.6.9'
elif version in ((3, 1), (3, 2)):
    required_sqlite = '3.7.0'
elif version == (3, 3):
    required_sqlite = '3.7.4'
elif version == (3, 4):
    required_sqlite = '3.8.2'
