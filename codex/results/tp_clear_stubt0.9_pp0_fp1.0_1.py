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

global latefin
assert callable(latefin)
del latefin

class OldStyle:
    pass

if isinstance(object, object):
    class OldStyle2(object):
        pass

class NonDeleting:
    """A class whose instances have a __del__ method that simply raises an
    exception.  This makes it harder for the reference-counting mechanism
    to immediately destroy the object, which is necessary in order to trigger
    the bug.
    """
    __slots__ = []
    def __del__(self):
        raise Exception

assert hash(NonDeleting()) == hash(NonDeleting())
assert hash(OldStyle()) != hash(OldStyle())
assert hash(OldStyle2()) != hash(OldStyle2())

print('Passed')
