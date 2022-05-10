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

if __name__ == "__main__":
    # On PyPy, gc.collect() forces the __del__ methods to run
    # before the test starts.  That's fine.
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
    start = time.time()
    for i in xrange(100000):
        if time.time() > start + 7:
            raise RuntimeError("too slow")
    gc.collect()
