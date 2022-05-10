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

latefin.ref()

# ____________________________________________________________

def f(x):
    return x + 1

def g(x):
    return f(x)

def h(x):
    return g(x)

def i(x):
    return h(x)

def j(x):
    return i(x)

def k(x):
    return j(x)

def l(x):
    return k(x)

def m(x):
    return l(x)

def n(x):
    return m(x)

def o(x):
    return n(x)

def p(x):
    return o(x)

def q(x):
    return p(x)

def r(x):
    return q(x)

def s(x):
    return r(x)

def t(x):
    return s(x)

def u(x):
    return t(x)

def v(x):
    return u
