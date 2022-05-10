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

#print func, latefin
#del func, latefin

#print func, latefin

def f():
    pass

def g():
    pass

#print f.__module__, g.__module__

def h():
    pass

def i():
    pass

def j():
    pass

def k():
    pass

def l():
    pass

def m():
    pass

def n():
    pass

def o():
    pass

def p():
    pass

def q():
    pass

def r():
    pass

def s():
    pass

def t():
    pass

def u():
    pass

def v():
    pass

def w():
    pass

def x():
    pass

def y():
    pass

def z():
    pass

def a():
    pass

def b():
    pass

def c():
    pass

def d():
    pass

def e():
    pass


