import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(0))]

c = C()
print(c.x)
ctypes.cast(c.x, ctypes.py_object).value = 42
print(c.x)

try:
    c.x = 42
except TypeError as e:
    print(e)

print(C.x)
print(type(C.x))
