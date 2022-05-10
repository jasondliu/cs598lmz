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

class A:
    pass

class B(A):
    pass

def f1(x):
    return x

def f2(x):
    return x

def f3(x):
    return x

def f4(x):
    return x

def f5(x):
    return x

def f6(x):
    return x

def f7(x):
    return x

def f8(x):
    return x

def f9(x):
    return x

def f10(x):
    return x

def f11(x):
    return x

def f12(x):
    return x

def f13(x):
    return x

def f14(x):
    return x

def f15(x):
    return x

def f16(x):
    return x

def f17(x):
    return x

def f18(x):
    return x

def f19(x):
    return x

def
