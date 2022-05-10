import ctypes
# Test ctypes.CField


class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]


class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.CField)]
    b = X()

# Test conversion to ctypes.CArgObject
import ctypes
# Test ctypes.CArgObject


class Int(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]


def func(arg):
    pass

func.argtypes = [ctypes.CArgObject(Int)]

# Test conversion to ctypes.CArray
import ctypes
# Test ctypes.CArray


class Int(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]


IntArray = Int * 10

def func(arg):
    pass

func.argtypes = [ctypes.CArray(Int)]

# Test conversion to ctypes.CPointer
import ctypes
# Test ctypes.CPointer


class Int(
