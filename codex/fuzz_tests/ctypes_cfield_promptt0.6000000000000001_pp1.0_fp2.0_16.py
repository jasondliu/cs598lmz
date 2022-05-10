import ctypes
# Test ctypes.CField.from_address()
import _ctypes_test
ll = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
class Array_2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 2)]
class Array_3(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 3)]
class Array_4(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 4)]
class Array_5(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 5)]
class Array_6(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 6)]
class Array_7(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 7)]
class Array_8(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 8)]
class Array
