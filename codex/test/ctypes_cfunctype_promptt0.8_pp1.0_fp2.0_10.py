import ctypes
# Test ctypes.CFUNCTYPE

class CF_TEST(ctypes.Structure):
    pass

CF_TEST_P = ctypes.POINTER(CF_TEST)

@ctypes.CFUNCTYPE(ctypes.c_int, CF_TEST_P)
def CF_TEST_FUNC(CF_TEST_P):
    return CF_TEST_P[0].value


CF_TEST_FUNC._argtypes_ = (CF_TEST_P,)
CF_TEST_FUNC._restype_ = ctypes.c_int

