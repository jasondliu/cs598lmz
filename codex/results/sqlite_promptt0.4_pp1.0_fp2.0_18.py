import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import os
import sys
import time
import unittest
import warnings

# For pickling support
try:
    import cPickle as pickle
except ImportError:
    import pickle

# For comparing exception details
try:
    import exception
except ImportError:
    # Python >= 2.6
    import traceback as exception

# For datetime and timedelta
import datetime

# For date and time
import time as _time

# For DECIMAL
import decimal

# For buffer
try:
    buffer
except NameError:
    # Python 3
    buffer = memoryview

# For NUMERIC
import sqlite3 as sqlite
sqlite.NUMERIC

# For detecting sqlite3.Connection and sqlite3.Cursor
sqlite3.Connection
sqlite3.Cursor

# For detecting sqlite3.PrepareProtocol
sqlite3.PrepareProtocol

# For detecting sqlite3.Row
sqlite3.Row

# For sqlite3.complete_statement
sqlite3.complete
