import ctypes
# Test ctypes.CField.
libm = ctypes.CDLL(ctypes.util.find_library("m"))
class TestCFloat(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double)]
# Test ctypes.CDLL.
libm = ctypes.CDLL(ctypes.util.find_library("m"))
# Test ctypes.CFuncPtr.
def func(a, b):
    return a - b
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
# Test ctypes.CFuncPtr.from_address.
def func(a, b):
    return a - b
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
FUNC_ADDR = ctypes.cast(FUNC, ctypes.c_void_p).value
FUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c
