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

# This is a regression test for a bug in the garbage collector.
# The bug was that the garbage collector would crash when it
# encountered a cyclic tuple that contained a function object.
# The bug was fixed by adding a special case to the garbage
# collector for function objects.

# The bug was originally found by running the test suite with
# the -R option.  The test suite was run with the following
# command line:
#
#    python -R Lib/test/regrtest.py test_gc
#
# The bug was fixed by applying the following patch:
#
# Index: Objects/funcobject.c
# ===================================================================
# RCS file: /cvsroot/python/python/dist/src/Objects/funcobject.c,v
# retrieving revision 1.1.1.1
# diff -c -r1.1.1.1 funcobject.c
# *** funcobject.c 2001/05/25 16:15:28 1.1.1.1
# --- funcobject.c 2001/05/25 16:16:00
#
