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
gc.collect()

# The following is a workaround for a bug in the way that the
# interpreter's finalization queue is managed.  If the bug is
# present, the interpreter will crash.  If the bug is not present,
# the interpreter will print "ok".

import weakref, gc

class A:
    pass

class B(A):
    pass

class C(A):
    pass

a = A()
b = B()
c = C()

w = weakref.ref(a)

del a, b, c
gc.collect()

if w() is None:
    print("ok")
