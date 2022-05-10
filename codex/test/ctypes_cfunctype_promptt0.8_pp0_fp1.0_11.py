import ctypes
# Test ctypes.CFUNCTYPE(return type, argument types...)
@ctypes.CFUNCTYPE(None)
def func0():
    return None

@ctypes.CFUNCTYPE(ctypes.c_int32)
def func1():
    return 1

@ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)
def func2(arg1):
    return arg1+1

@ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)
def func3(arg1, arg2):
    return arg1+arg2+1

@ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)
def func4(arg1, arg2, arg3):
    return arg1+arg2+arg3+1

