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
gc.collect()
del latefin
func()
</code>


A:

The following code can do it (it doesn't crash, at least):
<code>import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class LateTuple:

    def __del__(self):
        global func
        func = self[0]

class Cyclic(LateTuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])

cyc = tuple.__new__(Cyclic, (lambda : None, LateFin()))

cyc[0].__module__ = cyc
del cyc

gc.collect()
gc.collect()

func()
</code>
But it is extremely fragile.

