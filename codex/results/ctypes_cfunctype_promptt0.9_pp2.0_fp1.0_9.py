import ctypes
# Test ctypes.CFUNCTYPE
import ctypes

@CFUNCTYPE(c_int, c_int)
def cb_int_int(i):
    return -1

cb2 = cb_int_int(5)

# Test ctypes.PyDLL
import ctypes

msvcrt = ctypes.cdll.msvcrt

# Test ctypes.PyObj_FromPtr
import ctypes
import _ctypes

d = ctypes.PyObj_FromPtr(ctypes.addressof(_ctypes))
