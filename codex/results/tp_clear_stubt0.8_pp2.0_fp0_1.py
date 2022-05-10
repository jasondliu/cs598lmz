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
del func, cyclic, latefin

gc.collect()

# The del statement right before the collect()
# should register a weakref callback that releases
# the cyclic reference between cyc[0] and cyc[1].
#
# The __del__ method of cyc shouldn't actually be
# called until the next collect(), at which point
# it tries to mutate cyc[1] and store a weakref
# back to cyc[0].

import gc

gc.collect()

# This used to segfault, but now it's supposed
# to raise a TypeError for mutating a finalized
# object.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from test.support import run_unittest
run_unittest(__name__)
