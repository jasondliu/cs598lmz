import ctypes
# Test ctypes.CFUNCTYPE
######################################################################
addressof = ctypes.addressof

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def test(self):
        print("test")
x = X()
y = X()
cdecl = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
