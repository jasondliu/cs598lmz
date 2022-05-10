import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()

class B:
    pass

b = B()

def f():
    return a

def g():
    return b

def h():
    return a

def i():
    return b

def j():
    return a

def k():
    return b

def l():
    return a

def m():
    return b

def n():
    return a

def o():
    return b

def p():
    return a

def q():
    return b

def r():
    return a

def s():
    return b

def t():
    return a

def u():
    return b

def v():
    return a

def w():
    return b

def x():
    return a

def y():
    return b

def z():
    return a

def aa():
    return b

def ab():
    return a

def ac():
    return b

def ad():
    return a
