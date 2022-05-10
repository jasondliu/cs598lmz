import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time
import os
import sys
import re
import socket
import ssl
import email.utils
import subprocess
import pty
import fcntl
import struct
import signal
import select
import termios
import random
import atexit
from pwd import getpwnam
from grp import getgrnam
from . import _util
from . import _bplist
from . import _config
from . import _exceptions

LIB_PATH = None

def _find_lib_path():
    global LIB_PATH
    if LIB_PATH:
        return LIB_PATH
    paths = [
        "libusbmuxd.dylib",
        "libusbmuxd.so",
        "libusbmuxd.so.2"
    ]
    if sys.platform.startswith('linux'):
        paths.append(os.path.join(os.path.dirname(__file__), 'libusbmuxd.so.2'))
