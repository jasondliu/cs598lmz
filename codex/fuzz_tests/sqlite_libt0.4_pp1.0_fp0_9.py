import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import os
import sys
import time
import traceback
import subprocess
import re
import signal
import socket
import struct
import fcntl
import errno

# For python 2.5 compatibility
if not hasattr(__builtins__, 'any'):
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False

# For python 2.5 compatibility
if not hasattr(__builtins__, 'all'):
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True

# For python 2.5 compatibility
if not hasattr(__builtins__, 'set'):
    from sets import Set as set

# For python 2.5 compatibility
if not hasattr(__builtins__, 'basestring'):
    basestring = str

# For python 2.5 compatibility
if not hasattr(__builtins__, 'long'):
    long = int

# For python 2.5 compatibility

