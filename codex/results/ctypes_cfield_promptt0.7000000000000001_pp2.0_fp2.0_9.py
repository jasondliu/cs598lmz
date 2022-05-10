import ctypes
# Test ctypes.CField
class POLYNOMIAL(ctypes.Structure):
    _fields_ = [('a', ctypes.c_float), ('b', ctypes.c_float), ('c', ctypes.c_float)]

# Test ctypes.CPointer
POLY_ARRAY = POLYNOMIAL * 3

# Test ctypes.CArray
class POINT_ARRAY(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# Test ctypes.PYFUNCTYPE
@ctypes.PYFUNCTYPE(None)
def f():
    pass

# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(None)
def f():
    pass

# Test ctypes.WINFUNCTYPE
@ctypes.WINFUNCTYPE(None)
def f():
    pass

# Test ctypes.FunctionType
@ctypes.FunctionType(f)
def f():
    pass

# Test ctypes.Structure
