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


def f():
    x = 0
    def g():
        nonlocal x
        x += 1
        return x
    return g

def g1():
    x = 0
    def h():
        nonlocal x
        return x
    x += 1
    return h

def g2():
    x = 0
    def h():
        nonlocal x
        return x
    x += 1
    return h

def f2():
    x = 0
    def g():
        nonlocal x
        x += 1
        return x
    return g

def g3():
    x = 0
    def h():
        nonlocal x
        return x
    x += 1
    return h

def g4():
    x = 0
    def h():
        nonlocal x
        return x
    x += 1
    return h

def f3():
    x = 0
    def g():
        nonlocal x
        x += 1
        return x
    return g

def g5():
    x = 0

