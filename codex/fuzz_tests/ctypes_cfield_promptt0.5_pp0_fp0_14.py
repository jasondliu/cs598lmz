import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int, 1),
                ('c', ctypes.c_int, 1),
                ('d', ctypes.c_int)]
print X.a.offset
print X.b.offset
print X.c.offset
print X.d.offset

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int, 1),
                ('b', ctypes.c_int, 1),
                ('c', ctypes.c_int, 1),
                ('d', ctypes.c_int, 1)]
print X.a.offset
print X.b.offset
print X.c.offset
print X.d.offset

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int, 1),
                ('b', ctypes.c_int, 1),
                ('c', ctypes.c_int, 1),
                ('
