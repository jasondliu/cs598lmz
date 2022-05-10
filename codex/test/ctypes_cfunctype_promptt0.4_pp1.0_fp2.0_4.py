import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

import sys

def func(*args):
    print("func", args)

# cdecl calling convention
CFUNCTYPE_cdecl = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# stdcall calling convention
CFUNCTYPE_stdcall = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# fastcall calling convention
CFUNCTYPE_fastcall = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the default calling convention on Windows
CFUNCTYPE_default = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Test calling a function pointer

# cdecl calling convention
print("cdecl calling convention")
