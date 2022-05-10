import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool,ctypes.c_int,ctypes.c_int)
def set_callback(f):
    cb = FUNTYPE(f)
    lib.set_callback(cb)

def c_int(s):
    return ctypes.c_int(s)

def c_bool(s):
    return ctypes.c_bool(s)

def c_float(s):
    return ctypes.c_float(s)

# if __name__ == '__main__':
#     lib = ctypes.CDLL('./libpyinccall.so')
#     lib.set_callback.argtypes = [FUNTYPE]
#     lib.set_callback.restype = None
#     lib.test_callback.argtypes = [ctypes.c_int]
#     lib.test_callback.restype = ctypes.c_int
#     lib.test_callback2.argtypes = [ctypes.c_bool]
#     lib.test_callback2.restype = ctypes.c_bool
#
