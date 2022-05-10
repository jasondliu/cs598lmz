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

# This is a bit of a hack: we're relying on the fact that the
# weakref callback is called before the object is destroyed.  This
# isn't guaranteed by the docs, but it works on all the platforms I've
# tried.  It's needed to make sure that the weakref callback is
# invoked before the __del__ method on the class is invoked.  If the
# class's __del__ method gets invoked first, it will try to look up
# 'func', which no longer exists, and crash.
