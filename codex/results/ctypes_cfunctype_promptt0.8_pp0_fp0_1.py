import ctypes
# Test ctypes.CFUNCTYPE
#
# This tests the CFUNCTYPE object against the testapi.h header file.
#
# For some tests, we have to actually call the function.  To do this,
# we use CDLL(None), which is equivalent to dlopen(NULL).  The functions
# we need from this library (dlerror(), dlsym()) are actually defined in
# glibc and linked into the process executable.  This means that the
# CDLL(None) is not strictly portable.  It will work on the platforms
# that CPython supports, though.

import sys
import ctypes
from ctypes import *

TEST_DLL = CDLL(None)
TEST_DLL.dlerror.restype = c_char_p

# XXX This should be defined in a separate module
import _ctypes_test

def dlsym(name):
    result = TEST_DLL.dlsym(None, name)
    if not result:
        raise OSError(TEST_DLL.dlerror())
    return result

def check_type(
