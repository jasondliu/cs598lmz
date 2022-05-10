import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int32), ('y', ctypes.c_int32)]
p1 = POINT(10, 20)
p2 = POINT(30, 40)
# p1.x = 100 # AttributeError
a = POINT.x
a.__set__(p1, 100)
print(p1.x)

print(POINT.x.__get__(p1))

try:
    a.__set__(p1, 'abc')
except TypeError as e:
    print(repr(e))

print(POINT.x.__get__(p1, POINT))

print(POINT.x.__get__(p1, POINT))

print(POINT.x.__get__(p1, POINT))

print(POINT.x.__get__(p1, POINT))

print(POINT.x.__get__(p1, POINT))

print(POINT.x.__
