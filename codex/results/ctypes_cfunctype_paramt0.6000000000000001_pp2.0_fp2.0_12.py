import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.c_int, ctypes.c_int, ctypes.c_int)
f = FUNTYPE(lambda x, y, z: x+y+z)
f(1, 2, 3)

import ctypes
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
    lambda x, y: x+y)
f(1, 2)

import ctypes
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
f.restype = ctypes.c_int
f.argtypes = [ctypes.c_int, ctypes.c_int]
f(1, 2)

import ctypes
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
f.func_name = "my_func"
f.argtypes = [ctypes.c_
