import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__module__ = 'ctypes'

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

c = C()
print(c.x)
c.x = 42
print(c.x)

c.x = 'a'
print(c.x)

c.x = 'abc'
print(c.x)

c.x = '\xe9'
print(c.x)

c.x = '\xe9\xe9'
print(c.x)

c.x = '\xe9\xe9\xe9'
print(c.x)

c.x = '\xe9\xe9\xe9\xe9'
print(c.x)

c.x = '\xe9\xe9\xe9\xe9\xe9'
print(c.x)

c.x = '\xe9\xe9\xe9\xe9\xe9\xe9'
print(c.x)

