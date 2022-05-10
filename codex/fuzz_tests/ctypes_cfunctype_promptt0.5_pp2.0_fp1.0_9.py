import ctypes
# Test ctypes.CFUNCTYPE.
# This is a bit tricky to test, since we need to make sure that the
# correct calling convention is used.  We do this by creating a
# function that calls back into Python, and then make sure that the
# callback actually gets called.

import sys

if sys.platform == 'win32':
    stdcall = ctypes.WINFUNCTYPE
    cdecl = ctypes.CFUNCTYPE
else:
    stdcall = ctypes.CFUNCTYPE
    cdecl = ctypes.CFUNCTYPE

def func(a, b):
    print a, b
    return a + b

# Create a function with the stdcall calling convention.
FuncType = stdcall(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Call the function
f = FuncType(func)
res = f(1, 2)
assert res == 3

# Create a function with the cdecl calling convention.
FuncType = cdecl(ctypes.c_int, ctypes.c_int, ctypes
