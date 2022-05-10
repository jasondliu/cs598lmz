import ctypes
def py_func(x):
    return x + 1
C_func = ctypes.CFUNCTYPE(ctypes.py_object)(py_func)
print(C_func(1))
