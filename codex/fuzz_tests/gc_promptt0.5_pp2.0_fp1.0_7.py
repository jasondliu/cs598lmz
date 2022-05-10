import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class C:
    pass

def f():
    return C()

def g():
    return weakref.ref(C())

def h():
    return weakref.proxy(C())

class D(object):
    def __del__(self):
        pass

def i():
    return D()

def j():
    return weakref.ref(D())

def k():
    return weakref.proxy(D())

def l():
    return weakref.finalize(D(), lambda: None)

def m():
    return weakref.finalize(D(), lambda: None, D())

def n():
    return weakref.finalize(D(), lambda: None, D(), D())

def o():
    return weakref.finalize(D(), lambda: None, D(), D(), D())

def p():
    return weakref.finalize(D(), lambda: None, D(), D(), D(), D())

def q():
    return weakref.finalize(D(), lambda: None, D(), D(), D(),
