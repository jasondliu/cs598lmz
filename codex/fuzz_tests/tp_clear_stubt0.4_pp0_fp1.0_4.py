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
del func, cyc, LateFin, Cyclic
gc.collect()

# ____________________________________________________________

def g():
    pass

class C:
    pass

def f():
    g.__module__ = C

f()
gc.collect()

# ____________________________________________________________

def f():
    class C:
        pass
    C.__module__ = C

f()
gc.collect()

# ____________________________________________________________

def f():
    class C:
        pass
    C.__module__ = C.__module__

f()
gc.collect()

# ____________________________________________________________

def f():
    class C:
        pass
    C.__module__ = C.__module__.__class__

f()
gc.collect()

# ____________________________________________________________

def f():
    class C:
        pass
    C.__module__ = C.__module__.__class__.__module__

f()
gc.collect()

# ____________________________________________________________

def f():
    class C:
        pass

