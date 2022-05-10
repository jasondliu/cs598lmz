import ctypes
# Test ctypes.CFUNCTYPE
#
def func(x, y):
    return x + y

CF = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
f = CF(func)

f.argtypes = ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
f.restype = ctypes.POINTER(ctypes.c_int)
#
# This should be an error, assigning a function to a CFUNCTYPE instance
#f = CF(func)
#
# This should be an error, assigning the wrong function type to a CFUNCTYPE instance
#CF = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
#f = CF(lambda x, y: x + y)
#
#f.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
#f.restype = ctypes
