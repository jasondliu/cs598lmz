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

latefin = LateFin()

def g():
    global latefin
    latefin = LateFin()
    return None

def f():
    g()

for i in xrange(50):
    f()

print 'gc.collect() =', gc.collect()

del f, g

print 'gc.collect() =', gc.collect()

print 'gc.garbage =', gc.garbage

print 'func.__module__ =', func.__module__
print 'func.__module__.__class__ =', func.__module__.__class__
