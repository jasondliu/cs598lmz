import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    __slots__ = ['x', 'y']
    x = None
    y = None

def test():
    n = 2
    while n < 100:
        a = range(n)
        b = range(n)
        c = range(n)
        d = range(n)
        e = range(n)
        f = range(n)
        g = range(n)
        h = range(n)
        i = range(n)
        j = range(n)
        k = range(n)
        l = range(n)
        m = range(n)
        for i in range(n):
            a[i] = S()
            b[i] = S()
            c[i] = S()
            d[i] = S()
            e[i] = S()
            f[i] = S()
            g[i] = S()
            h[i] = S()
            i[i] = S()
            j[i] = S
