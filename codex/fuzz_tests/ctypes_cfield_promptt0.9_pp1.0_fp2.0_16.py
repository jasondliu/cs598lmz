import ctypes
# Test ctypes.CFields
import ctypes

class TestCF(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ubyte),
                ("b", ctypes.c_int)]

print type(TestCF.a), type(TestCF.b)
print TestCF(), TestCF.a, TestCF.b
print ctypes.sizeof(TestCF)
# Test ctypes.cdll.LoadLibray
from ctypes import *

# Variables

# If True, then the CDLL object is freed when it goes out of
# scope. 
#
# Normally, this would be a bad idea since the CDLL functions are
# not removed from memory, only their reference is removed.
#
# But here, the Lib class removes the CDLL dll's functions from
# memory.
free_DLLs = False


INVALID_HANDLE_VALUE = 0xFFFFFFFF

WIN32_FALSE = 0
WIN32_TRUE = 1


# Type Definitions
HANDLE = c_void_p

FARPROC = c_void
