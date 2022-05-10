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

# This is a test for the case where the __del__ method of a weakrefable
# object is called while the interpreter is deleting a module that
# contains the object.  In this case, the object's __del__ method
# shouldn't be called and the weakref should be left alive.

class A(object):
    def __del__(self):
        raise Exception

class B(object):
    def __del__(self):
        global a
        del a

a = A()
b = B()
a.x = weakref.ref(b)
del a, b
gc.collect()

# This is a test for the case where the __del__ method of a weakrefable
# object is called while the interpreter is deleting a module that
# contains the object.  In this case, the weakref shouldn't be left
# alive, but the weakrefable object's __del__ method shouldn't be called.

class A(object):
    def __del__(self):
        raise Exception

class B(object):
