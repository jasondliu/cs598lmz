import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class My_Structure(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_double),
                ('z', ctypes.c_double)]

def demo_structure():
    s = My_Structure()
    print(s.x, s.y, s.z)
    s.x = 100
    s.y = 2.5
    s.z = 3.14
    print(s.x, s.y, s.z)


class My_Union(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_double),
                ('z', ctypes.c_double)]

def demo_union():
    u = My_Union()
    u.x = 100
    print(u.x, u.y)
    u.z = 3.14
    print(u.x, u.y, u.z)

class Point(ctypes.Structure):
    _
