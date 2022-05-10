import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import re
import datetime
import inspect
import traceback
import unittest
import subprocess
import time
import platform
import collections
import inspect
import shutil
import tempfile
import errno

# Define some basic types
c_int = ctypes.c_int
c_int64 = ctypes.c_int64
c_uint64 = ctypes.c_uint64
c_size_t = ctypes.c_size_t
c_void_p = ctypes.c_void_p
c_char_p = ctypes.c_char_p
c_char = ctypes.c_char

# Get the platform specific libsqlite3 shared library
if sys.platform == "win32":
    libsqlite3_path = ctypes.util.find_library("sqlite3")
else:
    libsqlite3_path = ctypes.util.find_library("sqlite3")

# Load the libsqlite3 shared library
libsqlite3 = ctypes.CDLL(libsqlite3_path)

