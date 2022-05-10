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

# This is a bit tricky.  The LateFin instance is kept alive by the
# reference from the tuple, but the tuple is kept alive by the reference
# from the LateFin instance.  The LateFin instance is only freed when
# the tuple is freed.  The tuple is only freed when the LateFin instance
# is freed.  The LateFin instance is only freed when the tuple is freed.
# ...
# The tuple is only freed when the LateFin instance is freed.  The LateFin
# instance is only freed when the tuple is freed.  The tuple is only freed
# when the LateFin instance is freed.  ...
#
# The tuple is only freed when the LateFin instance is freed.  The LateFin
# instance is only freed when the tuple is freed.  The tuple is only freed
# when the LateFin instance is freed.  ...
#
# The tuple is only freed when the LateFin instance is freed.  The LateFin
# instance is only freed when the tuple is freed.  The tuple is only freed
# when the LateFin instance is freed.  ...
#
# The tuple
