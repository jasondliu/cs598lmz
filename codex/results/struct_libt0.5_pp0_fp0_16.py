import _struct
import _thread
import _threading
import _time
import _warnings
import _weakref
import atexit
import builtins
import functools
import imp
import marshal
import math
import posix
import pwd
import select
import signal
import sys
import time
import traceback

try:
    import _ctypes
except ImportError:
    _ctypes = None

try:
    import _multiprocessing
except ImportError:
    _multiprocessing = None

try:
    import _posixsubprocess
except ImportError:
    _posixsubprocess = None

try:
    import _socket
except ImportError:
    _socket = None

try:
    import _ssl
except ImportError:
    _ssl = None

try:
    import _tkinter
except ImportError:
    _tkinter = None

try:
    import _uuid
except ImportError:
    _uuid = None

try:
    import _winreg
except ImportError:
    _winreg = None

try
