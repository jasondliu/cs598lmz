import ctypes
ctypes.cast(None, ctypes.c_void_p).value

from ctypes import *
import string

def is_64bit():
    return sizeof(c_voidp) == 8

class String(Structure):
    _fields_ = [
        ("ptr", c_char_p),
        ("len", c_int),
    ]

class StringArray(Structure):
    _fields_ = [
        ("data", POINTER(String)),
        ("size", c_int),
    ]

def print_string_array(arr):
    for i in range(arr.size):
        s = arr.data[i]
        print s.ptr,

if is_64bit():
    dll = CDLL("bin/64/libstring.so")
else:
    dll = CDLL("bin/32/libstring.so")

dll.new_string.restype = POINTER(String)
dll.new_string.argtypes = [c_char_p]

dll.string_set_length.restype = c_int
dll.string
