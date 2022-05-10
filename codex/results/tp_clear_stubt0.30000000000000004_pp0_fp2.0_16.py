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

# ____________________________________________________________

def f():
    return 42

class A:
    def __del__(self):
        pass

class B(A):
    def __del__(self):
        f()

b = B()
b.__del__ = f
del b
gc.collect()

# ____________________________________________________________

class A:
    def __del__(self):
        pass

class B(A):
    def __del__(self):
        f()

b = B()
b.__del__ = f
b.__del__()
del b
gc.collect()

# ____________________________________________________________

class A:
    def __del__(self):
        pass

class B(A):
    def __del__(self):
        f()

b = B()
b.__del__ = f
b.__del__()
del b
gc.collect()

# ____________________________________________________________

class A:
    def __del__(self):
        pass

class B
