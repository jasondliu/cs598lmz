import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER

# This test passes on Windows, but fails on Linux.
# On Linux, the test crashes in the second call to
# the callback function.

import sys

import ctypes

def test_pointer():
    callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

    def callback(value):
        print("callback:", value[0])
        return value[0] + 1

    cb = callback_type(callback)
    result = cb(ctypes.byref(ctypes.c_int(42)))
    print("result:", result)
    assert result == 43

    result = cb(ctypes.byref(ctypes.c_int(43)))
    print("result:", result)
    assert result == 44

def test_pointer_to_pointer():
    callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)))


