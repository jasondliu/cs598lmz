import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import sys

def test(restype, argtypes, errcheck=None):
    func = ctypes.CFUNCTYPE(restype, *argtypes)(lambda *args: None)
    func.errcheck = errcheck
    func(1, 2, 3)

def test_errcheck(result, func, arguments):
    print(result)
    print(func)
    print(arguments)

# These should not raise an exception
test(None, [])
test(None, [ctypes.c_int])
test(None, [ctypes.c_int, ctypes.c_int])
test(None, [ctypes.c_int, ctypes.c_int, ctypes.c_int])
test(ctypes.c_int, [ctypes.c_int, ctypes.c_int, ctypes.c_int])
test(ctypes.c_int, [ctypes.c_int, ctypes.c_int, ctypes.c_int],
     test_errcheck)

# These should raise
