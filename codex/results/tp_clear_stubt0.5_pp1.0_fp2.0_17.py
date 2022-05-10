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
print(latefin)

# This one is a bit more tricky.
# It relies on the fact that when the interpreter is shutting down,
# the garbage collector is not run anymore.
# The garbage collector is run in the following cases:
# - when the "gc" module is used (e.g. gc.collect())
# - when a cyclic garbage collection occurs (e.g. when the reference count
#   of an object reaches zero)
# - when a list is resized
# - when a dict is resized
# - when a set is resized
# - when a deque is resized
# - when a file is closed
# The last case is the one we use here.

# Note that when a file is closed, the garbage collector is run only if
# the reference count of an object reaches zero.  This is why the
# 'LateFin' class is needed.

# The 'LateFin' class is used to create a reference to the 'func' object
# that is not part of a cycle.  When the 'LateFin' object is destroyed,
#
