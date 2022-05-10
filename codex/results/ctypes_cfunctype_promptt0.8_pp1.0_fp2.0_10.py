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

print("call func:", CF_TEST_FUNC(CF_TEST_P(3)))

# Test ctypes.Structure and ctypes.Union

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

@ctypes.CFUNCTYPE(ctypes.c_int, POINT)
def POINT_FUNC(POINT):
    return POINT.x +
