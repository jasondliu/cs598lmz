import ctypes
# Test ctypes.CFUNCTYPE
myCB1 = ctypes.CFUNCTYPE(ctypes.c_int)(lambda x, y: x + y)

class myClass(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

myCB2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(myClass))(lambda x: x.contents.x)

# Test ctypes.PYFUNCTYPE (typical use case)
myCB3 = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.POINTER(myClass))(lambda x: x.contents.x)

# Test ctypes.PYFUNCTYPE with keyword arguments
py_func_retval = 0
def py_func(*args, **kwargs):
    py_func_retval = kwargs['value']
    return py_func_retval

myCB4 = ctypes.PYFUNCTYPE(ctypes.c_int)(py_func)

