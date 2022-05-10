import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int),
                ('e', ctypes.c_int),
                ('f', ctypes.c_int),
                ('g', ctypes.c_int),
                ('h', ctypes.c_int)]

def main():
    c = C()
    c.a = 1
    c.b = 2
    c.c = 3
    c.d = 4
    c.e = 5
    c.f = 6
    c.g = 7
    c.h = 8
    for i in range(100000):
        c.a
        c.b
        c.c
        c.d
        c.e
        c.f
        c.g
        c.h

t = timeit.Timer(main)
print t.timeit(number=10)
