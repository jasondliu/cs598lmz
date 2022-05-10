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

# The following two were copied from test_weakref.py

class C:
    pass

def f(x=C()):
    print x

f()

def g():
    x = C()
    def h():
        print x
    return h

f2 = g()
f2()

# The following is from test_gc.py

class C:
    pass

def f():
    L = [C()]
    def g():
        L[0].x = L
        del L
    return g

f()()
