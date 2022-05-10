import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    class D(ctypes.Structure):
        _fields_ = [("bar", ctypes.c_int)]
c = C()
c.foo = 42
c.D.bar = 43
print c.foo, c.D.bar

# Test ctypes.CField.from_address
class E(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    class F(ctypes.Structure):
        _fields_ = [("bar", ctypes.c_int)]
e = E()
e.foo = 42
e.F.bar = 43
print e.foo, e.F.bar

# Test ctypes.CField.from_param
class G(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    class H(ctypes.Structure):
        _fields_ = [("bar", ctypes.c_int)]
g = G()
