import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char),
                ("y", ctypes.c_int),
                ("z", ctypes.c_char)]
    # This should have no effect if 'x' was already found:
    x = ctypes.CField("z")

print C.x
print C.y
print C.z
