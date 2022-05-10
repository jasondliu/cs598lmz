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
gc.garbage[0]()
# This will trigger the deletion of latefin, which resets func to a
# bound method which keeps cyc alive.
del func, cyc
gc.collect()
# That in turn triggers the deletion of cyc.  Deleting cyc involves
# deleting latefin.ref, which weakly references cyc[0], which
# ultimately weakly references cyc.  When cyc is deleted, latefin.ref
# must be set to None, but latefin.ref may have already been deleted.
gc.collect()
# In this final collection, latefin's __del__ method is invoked.  When
# latefin.ref is set to None a KeyError is raised, because latefin.ref
# has been deleted.  That KeyError is propagated through tp_del,
# tp_dealloc, type_dealloc, and object_dealloc, where it escapes into
# the wild, eventually hitting PyErr_WriteUnraisable.
import gc
gc.collect()
