import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 42

c = C()
print(c.x)
print(type(c.x))

c.x = S.x
print(c.x)
print(type(c.x))

c.x = S()
print(c.x)
print(type(c.x))

c.x = S.x(42)
print(c.x)
print(type(c.x))

c.x = S.x(S())
print(c.x)
print(type(c.x))

c.x = S.x(S.x(42))
print(c.x)
print(type(c.x))

c.x = S.x(S.x(S()))
print(c.x)
print(type(c.x))

c.x = ctypes.c_int(42)
print(c.x)
print(type(c.x))

c.x = ctypes.
