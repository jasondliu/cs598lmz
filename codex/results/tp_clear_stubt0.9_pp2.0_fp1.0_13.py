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

try:
  latefin.ref.__call__()
except ReferenceError:
  # This can happen, e.g. if Python's GC uses a different
  # strategy than CPython, but according to the latest Python
  # sources, CPython's GC can also free the function too soon.
  # If that happens, we get an exception in the weakref-call
  # above and we test the following field.
  #
  # It's not really good use to guard gc, hence the default option
  ctypesgen.gc_in_cython = False
else:
  # The above GC could have freed the function, but the weakref
  # should still exist
  assert latefin.ref
  func = int
  # Now Python's GC should no longer have a reference to func.
  # We *don't* succeed in freeing anything held by func, because
  # the weakref is still holding a reference to cyc, which contains
  # the cyc element which holds a reference to func.
  #
  # Anyway, the function object should have been
