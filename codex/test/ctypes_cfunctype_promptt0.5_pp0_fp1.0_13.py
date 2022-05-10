import ctypes
# Test ctypes.CFUNCTYPE
def Function(arg):
    return arg

FunctionPointer = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(Function)
assert FunctionPointer(42) == 42

# Test ctypes.PYFUNCTYPE
def PythonFunction(arg1, arg2, arg3):
    return arg1, arg2, arg3

PythonFunctionPointer = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(PythonFunction)
