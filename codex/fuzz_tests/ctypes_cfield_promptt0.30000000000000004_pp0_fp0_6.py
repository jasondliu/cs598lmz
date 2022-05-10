import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [('a', POINT),
                ('b', POINT)]

p = POINT(1, 2)
r = RECT(p, p)
print(r.a.x, r.a.y, r.b.x, r.b.y)

# Test ctypes.CArray
class Test(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 4)]

t = Test()
t.a[0] = 1
t.a[1] = 2
t.a[2] = 3
t.a[3] = 4
print(t.a[0], t.a[1], t.a[2], t.a[3])

# Test ctypes.CString
class Test(ctypes.Structure):
    _fields_ = [('a
