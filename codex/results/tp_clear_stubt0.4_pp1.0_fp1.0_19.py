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

# ____________________________________________________________

class A:
    pass

def f():
    pass

def g():
    pass

a = A()
a.__class__ = f
a.__class__ = g

# ____________________________________________________________

def f():
    pass

def g():
    pass

def h():
    pass

f.__module__ = g
f.__module__ = h

# ____________________________________________________________

def f():
    pass

def g():
    pass

def h():
    pass

f.__module__ = g
g.__module__ = h
f.__module__ = h

# ____________________________________________________________

def f():
    pass

def g():
    pass

def h():
    pass

f.__module__ = g
g.__module__ = h
f.__module__ = g

# ____________________________________________________________

def f():
    pass

def g():
    pass

def h():
    pass

f.__
