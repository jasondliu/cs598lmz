import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype_1():
    proto = [ctypes.c_void_p, ctypes.c_void_p]
    cfunc_type = ctypes.CFUNCTYPE(ctypes.c_int, *proto)

# Test ctypes.CFUNCTYPE
def test_cfunctype_2():
    proto = [ctypes.c_void_p, ctypes.c_void_p]
    cfunc_type = ctypes.CFUNCTYPE(ctypes.c_int, *proto)
    cfunc = cfunc_type(lambda x, y: x+y)

# Test ctypes.CFUNCTYPE
def test_cfunctype_3():
    proto = [ctypes.c_void_p, ctypes.c_void_p]
    cfunc_type = ctypes.CFUNCTYPE(ctypes.c_int, *proto)
    cfunc = cfunc_type(lambda x, y: x+y)
    cfunc(1, 2)

# Test
