import _struct
import _thread
import _threading_local
import _time
import _traceback
import _warnings
import _weakref
import _weakrefset
import array
import atexit
import binascii
import builtins
import errno
import faulthandler
import gc
import itertools
import marshal
import math
import operator
import posix
import reprlib
import select
import sys
import time
import unicodedata
import zlib

# Inline _thread module functions for performance

error = _thread.error
LockType = _thread.LockType
_start_new_thread = _thread.start_new_thread
_allocate_lock = _thread.allocate_lock
_get_ident = _thread.get_ident
_sleep = _thread._sleep

# Inline _struct for performance

calcsize = _struct.calcsize
pack = _struct.pack
unpack = _struct.unpack

# Inline _warnings for performance

warn = _warnings.warn

# Inline _weakref for performance


