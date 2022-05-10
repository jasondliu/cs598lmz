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
del latefin

# this is a bit tricky.  We have to make sure that func is not
# deallocated before the weakref callback is invoked.  The callback is
# invoked by the weakref machinery, but it may or may not be invoked
# before the refcount of func reaches zero.  The following code makes
# sure that func is not deallocated before the callback is invoked.

# XXX why do we need this?  Is there a race condition?

# the following makes sure that the weakref callback is invoked before
# func is deallocated.

# XXX this is a bit fragile.  We need to make sure that the callback
# is invoked before func is deallocated.  We also need to make sure
# that func is deallocated before the callback is invoked, otherwise
# we have a reference cycle.
import sys
if sys.platform == 'win32':
    # XXX why is this needed?  the function is not freed on win32 if we
    # don't do this.
    import time
    time.sleep(0.1)

del sys

