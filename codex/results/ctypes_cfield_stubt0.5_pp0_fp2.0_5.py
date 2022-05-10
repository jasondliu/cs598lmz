import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

c = C()
s = S.from_address(id(c))
assert s.x == 1
s.x = 2
assert c.x == 2

# Test that we can get an address from a subclass of CObject
class A(ctypes.c_int):
    pass

a = A()
assert ctypes.addressof(a) == id(a)

# Test that we can get an address from a subclass of Structure
class B(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

b = B()
assert ctypes.addressof(b) == id(b)
