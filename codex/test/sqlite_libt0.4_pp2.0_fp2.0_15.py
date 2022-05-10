import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import re
import string
import platform
import subprocess
import socket
import struct
import binascii
import traceback
import logging
import datetime
import json

from . import _lib

logger = logging.getLogger('pydivert')

class DivertException(Exception):
    pass

class DivertError(DivertException):
    pass

class DivertWarning(DivertException):
    pass

class DivertHandle(ctypes.Structure):
    _fields_ = [
        ('handle', ctypes.c_void_p),
        ('_lock', threading.Lock())
    ]

    def __init__(self):
        self.handle = None
        self._lock = threading.Lock()

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
