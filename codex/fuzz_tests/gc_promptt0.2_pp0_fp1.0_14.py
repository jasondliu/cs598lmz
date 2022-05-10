import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    c = C()
    c.x = c
    c.y = c
    c.z = c
    return c

def g():
    c = f()
    c.x = c
    c.y = c
    c.z = c
    return c

def h():
    c = g()
    c.x = c
    c.y = c
    c.z = c
    return c

def i():
    c = h()
    c.x = c
    c.y = c
    c.z = c
    return c

def j():
    c = i()
    c.x = c
    c.y = c
    c.z = c
    return c

def k():
    c = j()
    c.x = c
    c.y = c
    c.z = c
    return c

def l():
    c = k()
    c.x = c
    c.y = c
    c.z
