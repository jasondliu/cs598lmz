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

# This is a test for a bug in the garbage collector.  The bug was that
# the garbage collector would not call tp_clear on objects if they
# looked like they were part of a cycle, but weren't.  This is a
# problem if the object has something in its instance dict that needs
# to be cleared.

class A:
    def __init__(self):
        self.__dict__['x'] = 1

class B(A):
    def __del__(self):
        pass

a = A()
b = B()
b.__dict__ = a.__dict__
del a, b

gc.collect()

# This is a test for a bug in the garbage collector.  The bug was that
# the garbage collector would not call tp_clear on objects if they
# looked like they were part of a cycle, but weren't.  This is a
# problem if the object has something in its instance dict that needs
# to be cleared.

class A:
    def __init__(self):
        self.__
