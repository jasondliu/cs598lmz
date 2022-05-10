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
del func, cyc, LateFin, Cyclic


def g():
    latefin = None   # force __del__ of latefin, but not of cyc
    gc.collect()
    gc.collect()
    if func:
        yield True

gen = g()
assert gen.gi_frame.f_locals['func'] is func, repr(gen.gi_frame.f_locals)

try:
    next(gen)
except StopIteration as e:
    raise AssertionError("StopIteration should not have been raised")

try:
    next(gen)
except RuntimeError as e:
    assert type(e.__cause__) is ReferenceError, repr(e.__cause__)
else:
    raise AssertionError("RuntimeError should have been raised")

try:
    next(gen)
except RuntimeError as e:
    raise e
except StopIteration:
    pass
else:
    raise AssertionError("StopIteration should have been raised")
