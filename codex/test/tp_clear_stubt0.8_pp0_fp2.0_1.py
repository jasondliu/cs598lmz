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
assert not hasattr(LateFin, '__del__')

class A(tuple): pass
class B(tuple): pass

class X:
    def __del__(self):
        self.a = A()
        self.b = B()

def g():
    yield X()

def f(n):
    for i in range(n):
        g()

# Check whether the f_locals of the frame didn't contain
# a reference to the generator any longer.
#
# In Python 2.4 the f_locals of the frame was a dictionary,
# and it kept a reference to the generator; in 2.5 it became
# a weakrefable wrapper around a dictionary.
f(10)
gc.collect()
assert not hasattr(A, '__del__')
assert not hasattr(B, '__del__')


##### A test for issue #1394: a __del__ can trigger a
##### refleak, which shows up as a refleak during GC.

