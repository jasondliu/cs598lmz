import ctypes
# Test ctypes.CFUNCTYPE
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def PythonCall(x):
    return x

fptr = functype(PythonCall)
