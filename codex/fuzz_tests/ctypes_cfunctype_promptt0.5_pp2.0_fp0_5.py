import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the "call-conv" attribute, which is only available in
# the MSVC compiler, so only run this test on Windows.
if ctypes.sizeof(ctypes.c_void_p) == 4:
    # 32-bit
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = dll._testfunc_p_p
else:
    # 64-bit
    dll = ctypes.CDLL(None)
    func = dll.callproc


class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

# see issue 8287
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

def callback(x):
    y = Y()
    y.a = x.a * 2
    return y

CALL
