import ctypes
# Test ctypes.CFUNCTYPE

def func(a,b):
    return a+b

func_type = ctypes.CFUNCTYPE(ctypes.c_long,ctypes.c_long,ctypes.c_long)
func_type.func_name = 'func'
func_type.errcheck = ctypes.pythonapi.PyErr_CheckSignals

