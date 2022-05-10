import io
# Test io.RawIOBase
import ctypes
import ctypes.util
import sys
import threading
import unittest
import warnings
import weakref
from test import support

# If the OS has a C library, try to load it. If the attempt fails,
# that's okay, we'll just skip the tests that need it.
try:
    clib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
except (OSError, IOError) as err:
    if not getattr(err, 'winerror', None) == 126:
        # Windows error 126 means that the DLL was found, but loading it failed.
        # This is the case on some versions of Windows, which have a stub
        # c library and no real one.  In that case, the tests are still valid.
        raise
    clib = None

#
# Test the raw I/O implementation
#

class BaseTestIO(object):

    #subclassing_ok = False
    #file_closed_exc = IOError
    #invalid_op = 'invalid operation'

   
