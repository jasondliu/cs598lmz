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
func()

# Issue #17084: a __del__ method that raises an exception
# should only be called once.

class A(object):
    def __del__(self):
        raise Exception("should be called only once")

# Create a cycle with A.__del__ at the end.
a = A()
a.cycle = a
del a
gc.collect()

# Issue #17084: a __del__ method that raises an exception
# should not prevent other __del__ methods in the same cycle
# from being called.

l = []

class B(object):
    def __del__(self):
        l.append(self.id)

class C(object):
    def __del__(self):
        raise Exception("should not prevent other __del__ methods from being called")

# Create a cycle with C.__del__ at the end.
a = B()
a.id = 1
b = B()
b.id = 2
c = B()
c.id = 3
a.cycle = b

