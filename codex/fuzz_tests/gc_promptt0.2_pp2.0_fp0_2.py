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
    return weakref.ref(l)

def h():
    l = [1, 2, 3]
    l.append(l)
    return weakref.proxy(l)

def i():
    l = [1, 2, 3]
    l.append(l)
    return weakref.finalize(l, lambda: None)

def j():
    l = [1, 2, 3]
    l.append(l)
    return weakref.finalize(l, lambda: None, l)

def k():
    l = [1, 2, 3]
    l.append(l)
    return weakref.finalize(l, lambda: None, l, l)

def l():
    l = [1, 2, 3]
    l.append(l)
    return weakref.finalize(l, lambda
