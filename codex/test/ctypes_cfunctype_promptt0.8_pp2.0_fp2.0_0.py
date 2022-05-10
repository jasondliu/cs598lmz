import ctypes
# Test ctypes.CFUNCTYPE declaration
LP_c_int32_t = ctypes.POINTER(ctypes.c_int32)
py_cfoo = ctypes.CFUNCTYPE(ctypes.c_int32, LP_c_int32_t, LP_c_int32_t)

def test_cfoo(lib):
    lib.cfoo.argtypes = [ctypes.c_int32, ctypes.c_int32]
    lib.cfoo.restype = ctypes.c_int32

    args = [ctypes.c_int32.from_buffer(array.array("i", [6, 0]))]
    lib.cfoo(0, *args)

    # Test ctypes.CFUNCTYPE use
    cfoo = py_cfoo(lib.cfoo)
    args = [ctypes.c_int32.from_buffer(array.array("i", [6, 0]))]
    cfoo(0, *args)

