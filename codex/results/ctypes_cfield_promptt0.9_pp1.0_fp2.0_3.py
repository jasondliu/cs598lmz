import ctypes
# Test ctypes.CField.from_param()
from ctypes import _testcapi as testcapi

CFieldTest = testcapi.CFieldTest

# First define some helper functions:

class X(ctypes.Structure):
    _fields_ = [("value", ctypes.c_double, 5)]

class Y(ctypes.Structure):
    _fields_ = [("value", ctypes.c_double, 1)]

class Z(ctypes.Structure):
    _fields_ = [("head", ctypes.c_ulong), ("tail", ctypes.c_ulong)]

class CastingTest(ctypes.Structure):
    _fields_ = [
        ("x", X),
        ("y", ctypes.POINTER(Y)),
        ("z", Z),
        ("n", ctypes.c_int),
        ("s", ctypes.c_char)
    ]

def get_value(obj):
    if isinstance(obj, ctypes.Array):
        return obj[0]
    return obj.value

def create_double():

