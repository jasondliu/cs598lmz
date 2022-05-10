import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    # Common ancestor for both fields
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]
    class X:
        _type_ = ctypes.c_int
        _pack_ = True
        _other_ = None

    class Y:
        _type_ = ctypes.c_int
        _pack_ = True
        _other_ = None

    # Create the fields with the correct name and update the ancestors
    # dict for easy introspection
    x = ctypes.CField(X)
    y = ctypes.CField(Y)

p = POINT()
assert ctypes.sizeof(POINT) == ctypes.alignment(POINT) == ctypes.sizeof(p.x)
assert POINT.x.offset == ctypes.c_int.offset == 0
assert POINT.y.offset == ctypes.c_int.offset == ctypes.sizeof(ctypes.c_int)
p.x = -
