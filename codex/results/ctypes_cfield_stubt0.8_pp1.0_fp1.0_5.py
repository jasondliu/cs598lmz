import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    S.y = 4
except TypeError:
    pass
else:
    print("should not be able to add non-field attribute")

S = ctypes.Structure
S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S(1, 2)
print(s.x, s.y)

s.x = 3
s.y = 4
print(s.x, s.y)

try:
    s.x = "a string"
except TypeError:
    pass
else:
    print("should not be able to assign wrong type")

try:
    s.x = 5.5
except TypeError:
    pass
else:
    print("should not be able to assign wrong type")
