import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

cfunc = FUNTYPE(func)
print(cfunc(2))

# Create a C function pointer
cfunc = FUNTYPE(lambda x: x**2)
print(cfunc(2))

# Create a C function pointer from a C function
cfunc = FUNTYPE(ctypes.pythonapi.PyObject_Size)
print(cfunc(None))

# Create a C function pointer from a C function
cfunc = FUNTYPE(ctypes.pythonapi.PyObject_Size)
print(cfunc(None))

# Create a C function pointer from a C function
cfunc = FUNTYPE(ctypes.pythonapi.PyObject_Size)
print(cfunc(None))

# Create a C function pointer from a C function
cfunc = FUNTYPE(ctypes.pythonapi.PyObject_Size)
print(cfunc(None))

# Create a C function pointer from a C function
cfunc = FUNTYPE(ctypes.pythonapi.PyObject_
