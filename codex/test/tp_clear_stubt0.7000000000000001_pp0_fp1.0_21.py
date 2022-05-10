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

assert weakref.getweakrefcount(latefin) == 1
assert isinstance(latefin.ref(), type(lambda: None))

class WeakMethod:
    pass

class A:
    pass

a = A()
a.meth = WeakMethod()
a.meth.im_func = lambda:42
a.meth.im_self = a

w = weakref.ref(a.meth)
del a.meth
del a
gc.collect()

assert w() is None

class A:
    pass

a = A()
a.meth = WeakMethod()
a.meth.im_func = lambda:42
a.meth.im_self = a

w = weakref.ref(a)
w2 = weakref.ref(a.meth)
del a.meth
del a
gc.collect()

assert w() is None
assert w2() is None

class A:
    pass

a = A()
a.meth = WeakMethod()
