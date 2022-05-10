import ctypes
# Test ctypes.CField implementation

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('x', X),
                ('d', ctypes.c_int)]

py.test.raises(TypeError, ctypes.CField, None, None)
f = ctypes.CField(None, "a")
py.test.raises(TypeError, ctypes.CField, f, None)
f = ctypes.CField(None, "a")
py.test.raises(TypeError, ctypes.CField, f, 0)

f = ctypes.CField(None, ctypes.c_int, "a")
assert f.type_ == ctypes.c_int
assert f.offset == 0
assert f.size == 0
assert f.name == "a"

f = ctypes.CField(None, ctypes.c_int
