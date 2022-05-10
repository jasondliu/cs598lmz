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

# Disabling the GC is necessary to avoid the __del__ methods being called
# before this code is done with them.
gc.disable()

# It's important that the following code run in a different scope than above,
# or the __del__ method will be called before we're done with it.
def f():
    import sys
    del sys.modules['__main__']
    import __main__
    __main__.func()

f()
