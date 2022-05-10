import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def f():
    l = [1, 2, 3]
    l.append(l)
    return l

def g():
    l = [1, 2, 3]
    l.append(l)
    l = None

def h():
    l = [1, 2, 3]
    l.append(l)
    l = []

def i():
    l = [1, 2, 3]
    l.append(l)
    l.pop()

def j():
    l = [1, 2, 3]
    l.append(l)
    del l

def k():
    l = [1, 2, 3]
    l.append(l)
    l[:] = []

def l():
    l = [1, 2, 3]
    l.append(l)
    l[:] = l

def m():
    l = [1, 2, 3]
    l.append(l)
    l[:] = l[:]

def n():
    l = [1, 2, 3
