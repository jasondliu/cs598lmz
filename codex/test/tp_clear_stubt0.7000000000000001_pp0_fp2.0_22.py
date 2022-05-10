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
del latefin

# Testing a weakref to a function that has a weakref to it

def boo(): pass

def fin():
    global boo
    boo = f()

f = weakref.ref(boo, fin)
del boo
gc.collect()
del f

# Testing a weakref to a function that has a weakref to a class
# that has a weakref to it

def boo(): pass

def fin():
    global boo
    boo = f()

class A:
    __slots__ = ()
    def __del__(self):
        global boo
        boo = f()

f = weakref.ref(boo, fin)
a = A()
a.f = f
del boo, f
gc.collect()
del a

# Testing a weakref to a class that has a weakref to a function
# that has a weakref to it

def boo(): pass

def fin():
    global boo
    boo = f()

class A:
    __slots__ = ()
