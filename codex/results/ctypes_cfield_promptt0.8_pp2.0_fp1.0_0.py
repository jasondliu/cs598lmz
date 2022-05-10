import ctypes
# Test ctypes.CField:

class X(ctypes.Structure):
    _fields_ = [
        ("f1", ctypes.c_int),
        ("f2", ctypes.c_int)]

    class V(ctypes.Union):
        _fields_ = [
            ("m0", ctypes.c_double),
            ("m1", X),
            ("m2", ctypes.c_short)]

# Get the address of X.V.m1
POINTERS = (ctypes.POINTER(X), ctypes.POINTER(X.V))

def cast_addr(v):
    return (ctypes.cast(v, POINTERS[0]), ctypes.cast(v, POINTERS[1]))

# Define the offset of X.V.m1

assert X.V.m1.offset == 0

addr = cast_addr(ctypes.addressof(X.V.m1))
assert addr[0] == X.V.m1
assert addr[1] == X.V.m1
# Test ctypes.SField
