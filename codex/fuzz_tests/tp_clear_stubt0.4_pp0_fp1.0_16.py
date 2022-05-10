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

# The following code is executed by the Python interpreter,
# not by the test suite.  It is here to ensure that the
# weakref callback runs before the interpreter shuts down.
# The test suite doesn't wait for the callback to run.

# This is a bit of a hack, but it seems to work.

from time import sleep
sleep(0.1)
