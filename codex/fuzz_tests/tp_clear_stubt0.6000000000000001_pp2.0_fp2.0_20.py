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
func()

# This test is not interesting, because it doesn't need a weakref
# to break the cycle:
#
# >>> class Foo:
# ...   def __del__(self):
# ...     self.baz()
# ...
# >>> class Bar:
# ...   baz = Foo()
# ...
# >>> Bar.baz.__module__ = Bar
# >>> del Bar
# >>> gc.collect()
# >>>
#
# However, it's still interesting because it doesn't involve a
# function or a weakref, and it's a cycle.
