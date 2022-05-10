import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Nested(ctypes.Structure):
    _fields_ = [('a', S), ('b', S)]

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('n', Nested), ('c', C)]

def main():
    d = D()
    d.n.a.x = 1
    d.n.b.x = 2
    d.c.x = 3
    d.c.y = 4

    print(d.n.a.x, d.n.b.x, d.c.x, d.c.y)
    print(type(d.n.a.x), type(d.n.b.x), type(d.c.x), type(d.c.y))
    print(type(d.n.a), type(d.n.b), type(d.c))
    print(type(d.n),
