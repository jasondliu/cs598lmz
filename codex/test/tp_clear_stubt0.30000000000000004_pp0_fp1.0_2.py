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

class Sub(object):
    __slots__ = ('__weakref__',)

class Base(object):
    __slots__ = ('__weakref__',)

class SubSub(Sub):
    __slots__ = ()

class SubSubSub(SubSub):
    __slots__ = ()

a = Base()
b = Sub()
c = SubSub()
d = SubSubSub()

a.__class__ = Sub
b.__class__ = SubSub
c.__class__ = SubSubSub
d.__class__ = Base

gc.collect()

