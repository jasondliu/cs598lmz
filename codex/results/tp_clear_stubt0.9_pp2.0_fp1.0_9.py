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
latefin.ref().__name__
</code>
or
<code>import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class CycTuple:
    __slots__ = ()
    def __new__(cls, sequence):
        res = tuple.__new__(CycTuple, sequence)
        res.ref = weakref.ref(res)
        return res

func = lambda: None
cyc = CycTuple((func, LateFin()))

func.__module__ = cyc
del func, cyc

gc.collect()
latefin.ref().__name__
</code>


A:

No, there's no way to create a cyclic object that remains alive and correctly referenced until a garbage collection happens, when it is deleted.
This is because the garbage collector is allowed to delete the object at any time, as soon as it has detected that the object is no longer strongly referenced
