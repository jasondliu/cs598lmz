import ctypes

class S(ctypes.Structure):
    x = 23
    _fields_ = [('a', ctypes.c_int32),
                ('b', ctypes.c_int32),
                ('c', (ctypes.c_int32 * 2))]

def test():
    s = S(1, 2, (3, 4))
    print s.a, s.b, s.c[0], s.c[1]
    s = S((1, 2, 5, 6, 4, 3))
    print s.a, s.b, s.c[0], s.c[1]
    S2 = S * 7
    s = S2()
    print s[6].a, s[6].b, s[6].c[0], s[6].c[1]
    s = S2((1, 2, 5, 6, 4, 3),(1, 2, 5, 6, 4, 3))
    print s[0].a, s[0].b, s[0].c[0], s[0].c[1]
    print s[1].a, s[1].
