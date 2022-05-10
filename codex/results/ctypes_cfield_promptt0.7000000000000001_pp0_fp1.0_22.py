import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# Test ctypes.CField pointer
class POINTP(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

# Test ctypes.CField array
class POINTARRAY(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 2)]

# Test ctypes.CField struct
class RECT(ctypes.Structure):
    _fields_ = [('a', POINT), ('b', POINT)]

# Test ctypes.CField pointer to struct
class RECTP(ctypes.Structure):
    _fields_ = [('a', ctypes.POINTER(POINT))]

# Test ctypes.CField struct array
class RECTARRAY(ctypes.Structure):
    _fields_ = [('a', POINT * 2)]

# Test ctypes.C
