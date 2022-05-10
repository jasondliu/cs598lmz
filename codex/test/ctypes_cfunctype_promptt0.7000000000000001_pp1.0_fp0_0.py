import ctypes
# Test ctypes.CFUNCTYPE
def pyfunc(a, b):
    print("python function called with %r and %r" % (a, b))
    return a + b

# the CFUNCTYPE constructor takes types instead of python objects
# int, int -> int
# We can use ctypes.c_int32 instead of Python int types.
PyObject_Call = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)(pyfunc)

print("CFUNCTYPE: calling python function:", PyObject_Call(1, 2))

# Test ctypes.PYFUNCTYPE
# PYFUNCTYPE is used to specify return type as py_object.
PyObject_Call = ctypes.PYFUNCTYPE(ctypes.py_object, ctypes.c_int32, ctypes.c_int32)(pyfunc)
print("PYFUNCTYPE: calling python function:", PyObject_Call(1, 2))

# Test ctypes.WINFUNCTYPE
# Win
