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
del latefin
gc.collect()
</code>
This is the full source code, which will be <code>trimmed()</code>:
<code>import gc, weakref, imp

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

def trim_funcs(latefin, cyclic, func):
    @cycles(cyclic)
    @cycles(func)
    def inner():
        cyclic[1].ref = weakref.ref(cyclic[0])
        del latefin
    inner()

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
trim_funcs(latefin
