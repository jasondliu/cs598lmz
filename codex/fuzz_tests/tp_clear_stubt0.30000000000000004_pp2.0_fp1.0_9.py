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

# This should not crash, but it does.
# The problem is that the module object is not cleared,
# so when the module is cleared, the module object is cleared,
# and the module object is cleared, and so on.
#
# The module object is not cleared because it is still
# referenced by the function object, which is not cleared
# because it is still referenced by the module object.
#
# The problem is that the module object is not cleared
# because it is still referenced by the function object,
# which is not cleared because it is still referenced
# by the module object.
#
# The problem is that the module object is not cleared
# because it is still referenced by the function object,
# which is not cleared because it is still referenced
# by the module object.
#
# The problem is that the module object is not cleared
# because it is still referenced by the function object,
# which is not cleared because it is still referenced
# by the module object.
#
# The problem is that the module object is not cleared
# because it is still referenced by the function object,
