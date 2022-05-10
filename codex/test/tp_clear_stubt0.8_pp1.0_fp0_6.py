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

class MyDesc:
    def __get__(self, obj, type):
        raise gc.CollectableError

def new():
    x = MyDesc()
    func = lambda: x
    func.__module__ = x
    return func

f = new()
func(lambda: f)
del f
gc.collect()

class MyDesc:
    def __get__(self, obj, type):
        global func
        del func
        return 42

def new():
    x = MyDesc()
    func = lambda: x
    func.__module__ = x
    return func

f = new()
func(lambda: f)
del f
# We used to crash here with a segfault

class D(dict):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def __del__(self):
        pass

d = D()
d.__dict__ = d
def f():
    d.a

