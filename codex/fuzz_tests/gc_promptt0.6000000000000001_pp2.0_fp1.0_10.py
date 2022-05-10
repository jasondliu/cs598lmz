import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a cyclic list with a finalizer.

def f(x):
    pass

def g(x):
    pass

class C:
    _finalizing = False
    def __del__(self):
        self._finalizing = True

for i in range(10000):
    a = C()
    b = C()
    a.x = b
    b.x = a
    a.y = [a, b]
    b.y = a.y
    a.y = a.y
    f(a)
    f(b)
    a._finalizing = False
    b._finalizing = False
    del a
    del b
    gc.collect()
    if a._finalizing or b._finalizing:
        raise TestFailed("finalization occurred")
