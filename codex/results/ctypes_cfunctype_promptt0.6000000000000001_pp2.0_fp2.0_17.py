import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import CFUNCTYPE, c_int, c_float
if not hasattr(ctypes, 'c_double'):
    ctypes.c_double = c_float

# Test ctypes.POINTER(t)
from ctypes import POINTER, pointer

# Test ctypes.byref(o)
from ctypes import byref, addressof

# Test ctypes.string_at(o[, size])
from ctypes import string_at

# Test ctypes.wstring_at(o[, size])
from ctypes import wstring_at

# Test ctypes.get_errno()
from ctypes import get_errno

# Test ctypes.set_errno(code)
from ctypes import set_errno

# Test ctypes.create_string_buffer(init, size)
from ctypes import create_string_buffer

# Test ctypes.create_unicode_buffer(init, size)
from ctypes import create_unicode_buffer

# Test ctypes.wstring_at(o[, size
