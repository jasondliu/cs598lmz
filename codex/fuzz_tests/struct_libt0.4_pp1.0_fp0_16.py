import _struct
import _thread
import _threading_local
import _time
import _warnings
import _weakref
import array
import atexit
import audioop
import binascii
import builtins
import cmath
import errno
import faulthandler
import gc
import grp
import itertools
import math
import mmap
import operator
import parser
import resource
import select
import signal
import sys
import threading
import time
import unicodedata
import zlib

# these modules are optional and may not be present
try:
    import _curses
except ImportError:
    pass

try:
    import _curses_panel
except ImportError:
    pass

try:
    import _hashlib
except ImportError:
    pass

try:
    import _multibytecodec
except ImportError:
    pass

try:
    import _multiprocessing
except ImportError:
    pass

try:
    import _posixsubprocess
except ImportError:
    pass

try:
    import _socket

