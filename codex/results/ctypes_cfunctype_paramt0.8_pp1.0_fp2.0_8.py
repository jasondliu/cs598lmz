import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

class A:
    def __init__(self, i):
        self.i = i
    def f(self):
        print('f', self.i)
        return self.i
    def g(self):
        print('g', self.i)
        return self.i

a = A(0)
a.f = FUNTYPE(a.f)

for i in range(1, 5):
    setattr(a, 'f%d' % i, a.f)
    setattr(a, 'g%d' % i, a.g)

def h(self):
    return self.i

setattr(a, 'h', h)

for i in range(1, 5):
    setattr(a, 'h%d' % i, h)

for i in range(1, 5):
    print(getattr(a, 'f%d' % i)())

for i in range(1, 5):
    print(getattr(a, 'g%d' % i)
