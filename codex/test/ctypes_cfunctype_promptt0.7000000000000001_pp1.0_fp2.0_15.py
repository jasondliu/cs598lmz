import ctypes
# Test ctypes.CFUNCTYPE(<type>)
print(ctypes.CFUNCTYPE(ctypes.c_int)())
# Test ctypes.CFUNCTYPE(<type>,...)
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)())
# Test ctypes.CFUNCTYPE(<type>,...)(<function>)
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)(1, 2))
# Test ctypes.CFUNCTYPE(<type>,...)(<function>, <function>)
