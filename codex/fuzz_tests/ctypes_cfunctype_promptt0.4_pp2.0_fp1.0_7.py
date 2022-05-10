import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the function we will be calling.
PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we will be calling.
def py_func(n):
    return n * 2

# Convert the Python function to a C callback.
c_func = PROTOTYPE(py_func)

# Call the C callback via the ctypes callback.
assert c_func(42) == 84

# Call the C callback directly.
assert ctypes.pythonapi.PyCFuncPtr_Type.mro()[-2]._call_(c_func.ptr, 42) == 84

# Test ctypes.WINFUNCTYPE

# This is the prototype of the function we will be calling.
PROTOTYPE = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we will be calling.
def py_func(n):
    return n * 2

# Convert the Python function to
