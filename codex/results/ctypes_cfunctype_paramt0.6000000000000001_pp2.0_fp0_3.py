import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(i):
    print("Python function called with", i)
    return 0

CMPFUNC = FUNTYPE(py_func)

# Import the library
lib = ctypes.cdll.LoadLibrary('./libexample.so')

# Set the argtypes and restype
lib.call_with_int.argtypes = [FUNTYPE]
lib.call_with_int.restype = ctypes.c_int

# Call the C function
lib.call_with_int(CMPFUNC)
