import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

import time
# Test time.clock()
time.clock()

import threading
# Test threading.Lock()
threading.Lock()

import ctypes
# Test ctypes.Structure()
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
X()

import ctypes.util
# Test ctypes.util.find_library()
ctypes.util.find_library("m")

import _ctypes
# Test _ctypes.dlopen()
_ctypes.dlopen("libm.so", _ctypes.RTLD_GLOBAL)

import _testcapi
# Test _testcapi.INT_MAX
_testcapi.INT_MAX

# Test _testcapi.INT_MIN
_testcapi.INT_MIN

# Test _testcapi.UINT_MAX
_testcapi.UINT_MAX

# Test _testcapi
