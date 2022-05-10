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
print(latefin.__del__.__globals__)

# Issue #10451: test that the finalizer is called even if an exception is
# raised.
class Cyclic:
    def __del__(self):
        raise Exception

def f():
    c = Cyclic()
    c.x = c
f()
gc.collect()

# Issue #10451: test that the finalizer is called even if the finalizer
# itself raises an exception.
class Cyclic:
    def __del__(self):
        raise Exception

def f():
    c = Cyclic()
    c.x = c
    del c
f()
gc.collect()

# Issue #10451: test that the finalizer is called even if the finalizer
# itself raises an exception and the exception is caught.
class Cyclic:
    def __del__(self):
        raise Exception

def f():
    try:
        c = Cyclic()
        c.x = c
    except:
        pass
f()
gc.collect()
