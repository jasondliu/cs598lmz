import ctypes
# Test ctypes.CField
class CFoo(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_int)]
    class C(ctypes.Structure):
        _fields_ = [("foobar", ctypes.c_int)]
    c = C()

f = CFoo()
f.c.foobar = 42
print(f.c.foobar)
