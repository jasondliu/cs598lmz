import ctypes
# Test ctypes.CFUNCTYPE() with a function that returns a pointer.

import ctypes
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that returns a pointer to the string "Hello World".
restype = ctypes.POINTER(ctypes.c_char)
func = lib.return_string
func.restype = restype
print(func())
print(func.restype)
print(ctypes.cast(func(), restype).contents.value)

func = lib.return_string
func.restype = ctypes.c_char_p
print(func())
print(func.restype)
print(func())

restype = ctypes.POINTER(ctypes.c_char)
func = lib.return_string
func.restype = restype
func.__name__ = "return_string"

# This should call PyCFunction_Call.  A CFUNCTYPE function never returns
# NULL.
print(func())
print(func.restype)
print(ctypes.cast
