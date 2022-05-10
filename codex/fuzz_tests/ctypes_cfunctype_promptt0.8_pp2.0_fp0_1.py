import ctypes
# Test ctypes.CFUNCTYPE().

import _ctypes_test

try:
    rffi.cast(ctypes.CFUNCTYPE(ctypes.c_int), 0)
except ValueError as e:
    print("ValueError:", e)

try:
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(0)
except ValueError as e:
    print("ValueError:", e)

try:
    ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 0)
except ValueError as e:
    print("ValueError:", e)


# Test ctypes.WinError.

import sys

prev_err = ctypes.get_last_error()

ctypes.WinError()
ctypes.WinError(0)
ctypes.WinError(12345678)

try:
    raise ctypes.WinError()
except OSError as e:
    print("OSError:", e)
    print(e.winerror, e.strerror)

try:
