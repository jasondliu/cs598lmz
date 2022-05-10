import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def g():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def h():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def i():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def j():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def k():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def l():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def m():
    class C:
        pass
    c = C()
    return weakref.ref(c)

def n():
    class C:
        pass
    c = C()
    return weak
