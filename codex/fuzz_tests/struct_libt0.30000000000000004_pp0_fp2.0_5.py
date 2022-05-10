import _struct
import _thread
import _threading_local
import _warnings
import _weakref
import _weakrefset
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
import marshal
import math
import mmap
import operator
import parser
import posix
import pwd
import pyexpat
import select
import signal
import sys
import time
import unicodedata
import xxsubtype

# These modules are not built by default, but we want to make sure that
# the Python code for them is always present in the standard library.
import _testbuffer
import _testimportmultiple
import _testmultiphase
import _xxlimited

# These modules are only built if the corresponding shared library
# is available.
try:
    import _bz2
except ImportError:
    pass

try:
    import _curses
except ImportError:
    pass

try:
    import _curses_panel
except ImportError:
