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

# print(latefin.ref)

assert latefin.ref() is None
"""

# test_gc_collect_cyclic_weakrefs
# Issue #31225: check that cyclic weakrefs are collected at shutdown.

from test.support import gc_collect, gc_collect_harder

from weakref import WeakSet

class Obj:
    pass

objs = [Obj() for i in range(10)]
wset = WeakSet(objs)

# Keep objs alive until after gc.collect()
keepalive = [objs]


gc_collect()
assert wset == set(objs)

gc_collect_harder()
assert wset == set(objs)

del keepalive
gc_collect_harder()
assert not wset


# Issue #31225: check that cyclic weakrefs with callbacks are collected at shutdown.

from test.support import gc_collect, gc_collect_harder

from weakref import WeakSet, ref

class Obj
