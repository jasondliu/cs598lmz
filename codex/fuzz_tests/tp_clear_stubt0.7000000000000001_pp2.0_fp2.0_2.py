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
del func, cyc, latefin

gc.collect()

def f(): pass

def g(): return 1

def h():
    return (1,2,3)

def i():
    return [1, 2, 3]

def j():
    return 1, 2, 3

def k():
    return 1 if True else 2

def l():
    return True or False

def m():
    return True and False

def n():
    return not False

def o():
    return True ^ False

def p():
    return 3 >> 1

def q():
    return 3 << 1

def r():
    return 3 | 1

def s():
    return 3 ^ 1

def t():
    return 3 & 1

def u():
    return 3 + 1

def v():
    return 3 - 1

def w():
    return 3 * 1

def x():
    return 3 / 1

def y():
    return 3 // 1

def z():
    return 3 % 1

def aa():
    return 3 ** 1
