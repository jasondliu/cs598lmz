import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect at startup due is a segfault on Debian (3.8.2-1ubuntu4)
sqlite3.connect(':memory:').close()

__all__ = ['libX11', 'X11Error', 'X11Selection']

try:
    libX11 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('X11'))
except OSError as e:
    raise X11Error('Could not find libX11')

# Some platforms/versions don't define Display etc., so define them ourselves.

Display = POINTER(c_void_p)
Window = c_ulong
Time = c_ulong
Atom = c_ulong


# Bool.
#
# Define the type here, because ctypes.c_bool doesn't work on old versions of
# Python.
#
# On 64-bit platforms, casts to Bool implicitly sign-extend and casts from Bool
# implicitly zero-extend, i.e.,
#
#   >>> ctypes.cast(2**63, ctypes.c_
