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
print(latefin.ref() is None)
print(func is None)

# test __del__ in a weakrefable class
class A:
    def __del__(self):
        pass

class B(A):
    pass

a = A()
b = B()
a.b = b
b.a = a

del a, b
gc.collect()

# test __del__ in a weakrefable class with a __slots__
class A:
    __slots__ = ()
    def __del__(self):
        pass

class B(A):
    __slots__ = ()

a = A()
b = B()
a.b = b
b.a = a

del a, b
gc.collect()

# test __del__ in a weakrefable class with a __slots__ and a __dict__
class A:
    __slots__ = ()
    def __del__(self):
        pass

class B(A):
    __slots__ = ()
