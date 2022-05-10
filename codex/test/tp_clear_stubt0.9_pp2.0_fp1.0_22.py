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
del LateFin, Cyclic
gc.collect()

def func_wrapper(f):
    def wrapper(*args):
        global f
        f = f()
        return f(*args)
    return wrapper

func = func_wrapper(func)
del func_wrapper

def f(b):
    if not b:
        return 1
    return f(b-1)

del latefin
print(f(100_000))
