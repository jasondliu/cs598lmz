import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(a, b):
    return a + b

lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

#lib.add(1, 2)

#lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
#lib.add.restype = ctypes.c_int
#lib.add(1, 2)

#lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
#lib.add.restype = ctypes.c_int
#lib.add(1, 2)

#lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
#lib.add.restype = ctypes.c_int
#lib.add(1, 2)

#lib.add.argtypes = [ctypes.c_int, ctypes
