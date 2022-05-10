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
gc.collect()

# Check that the late-deletion mechanism doesn't crash.
# (It used to, because the late-deletion mechanism didn't
#  handle weakrefs to objects in the garbage collector's
#  list of objects to be deleted.)

# XXX: This test is disabled because it fails with PyPy.
#      See https://bitbucket.org/pypy/pypy/issue/2062/
#      for more details.
#
#      The test is also disabled because it fails with
#      CPython 3.3.  See http://bugs.python.org/issue17094
#      for more details.

#import gc
#import weakref
#
#class A:
#    pass
#
#class B:
#    pass
#
#a = A()
#b = B()
#a.b = b
#b.a = a
#
#a_ref = weakref.ref(a)
#b_ref = weakref.ref(b)
#
#del
