import _struct
import _unicodedata
import _warnings
import _weakref
import array
import atexit
import builtins
import errno
import fcntl
import gc
import itertools
import marshal
import math
import operator
import posix
import pwd
import signal
import sys
import time
import zlib

# All CPython built-in modules that we emulate.
BUILTIN_MODULES = (
    _thread, _codecs, _collections, _functools, _hashlib, _imp, _io, _locale, _operator,
    _signal, _sre, _stat, _string, _struct, _unicodedata, _warnings, _weakref,
    array, atexit, errno, fcntl, gc, itertools, marshal, math, operator, posix, pwd, signal, sys, time, zlib
)

# The following modules are not part of the standard library and are not
# provided by MicroPython.
