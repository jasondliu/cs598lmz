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
del func, cyc, LateFin, Cyclic
gc.collect()
"""

# When a cycle is broken and the object is freed immediately,
# it's possible for the __del__ method to run with a weakref
# to the object that created the cycle.  In this case (via
# randomization) the object is the module object.
#
# Run the above code with a single argument:
#
#  -p: test that the module is freed without running a __del__ method
#  -c: test that the module is freed, but a cycle is created,
#      and that the __del__ method eventually runs
#  -g: test that the module is only freed when all globals are freed
#
# The -c and -g options test the same basic code, but the -c option
# triggers the problem on every run, while the -g option requires
# garbage collection of the global scope.  The -c option must
# be used to test the fix for the bug, but the -g option requires
# less memory to run.

import sys, gc

if len(sys.argv) == 1 or
