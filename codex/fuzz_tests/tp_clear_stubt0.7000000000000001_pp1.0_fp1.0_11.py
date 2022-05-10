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

# The second gc.collect() should be necessary in order to break the cycle,
# but it isn't because the __del__() method of tuple doesn't call gc.collect().
gc.collect()

# This should not raise any exception, because func should not be garbage.
func()

# This should not raise any exception, because func should not be garbage.
# It works in 2.6.1 and 3.1.2, but fails in 2.5.4 with a RuntimeError:
# "unidentifiable C object"
assert func() is None
