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
# verify that the __del__ method was called
assert latefin.ref() is not None

# Issue #23585: during finalization of an object, the garbage collector
# could consider methods of the object as being uncollectable.  If
# another object is finalized during the process, and refers to an
# attribute of the first object, then that attribute could be cleared
# while the garbage collector is attempting to decref it.  That would
# trigger a fatal error in the assert() in PyObject_ClearWeakRefs()
# (see issue #20485).

class A:
    def __del__(self):
        del self.attr

class B:
    def __del__(self):
        A().attr = self

a = A()
a.attr = B()
del a
gc.collect()

# Issue #23976: if an object's weakrefs are cleared while a reference
# to the object is held by an object being finalized, the garbage
# collector could crash when decref'ing the object.

