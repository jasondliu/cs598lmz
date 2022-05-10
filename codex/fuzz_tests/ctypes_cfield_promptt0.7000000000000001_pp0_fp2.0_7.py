import ctypes
# Test ctypes.CField object
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

pt = POINT(1, 2)
print(pt.x, pt.y)
pt.x = 3
print(pt.x, pt.y)

# Test ctypes.CField.__get__
class P(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class C:
    pass

c = C()
c.p = P(1)
print(c.p.x)
c.p.x = 2
print(c.p.x)

# Test ctypes.CField.__set__
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

pt = POINT(1, 2)
print(pt.x, pt.y)
pt.x = 3
print(pt.x, pt.y
