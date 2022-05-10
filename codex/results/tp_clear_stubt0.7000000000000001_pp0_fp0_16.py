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
assert latefin.ref() is None
del latefin

# Check that the weakref destructor is run with the right globals

globals = {}

class MyWeakRef:
    def __init__(self, ob):
        self.ref = weakref.ref(ob, self.check)

    def check(self, ref):
        global globals
        globals = globals1

globals1 = {}
globals2 = {}

wr = MyWeakRef(globals)
del wr

del globals1, globals2
gc.collect()

assert globals == {}

# Check behaviour when the referent is a class

class A:
    pass

class B(object):
    pass

x = A()
wr = weakref.ref(x)
assert wr() is x

y = B()
wro = weakref.ref(y)
assert wro() is y
