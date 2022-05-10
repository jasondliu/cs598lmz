import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

class A(object):
    def __del__(self):
        self.b.c = None

class B(object):
    def __del__(self):
        self.c.a = None

class C(object):
    def __del__(self):
        self.a.b = None

a = A()
b = B()
c = C()

a.b = b
b.c = c
c.a = a

del a, b, c
gc.collect()
