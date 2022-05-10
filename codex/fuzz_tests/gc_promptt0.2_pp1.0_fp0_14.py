import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    l = [1, 2, 3]
    l.append(l)
    return l

def g():
    l = f()
    l.append(l)
    return l

def h():
    l = g()
    l.append(l)
    return l

def i():
    l = h()
    l.append(l)
    return l

def j():
    l = i()
    l.append(l)
    return l

def k():
    l = j()
    l.append(l)
    return l

def l():
    l = k()
    l.append(l)
    return l

def m():
    l = l()
    l.append(l)
    return l

def n():
    l = m()
    l.append(l)
    return l

def o():
    l = n()
    l.append(l)
    return l

def p():
    l = o()
    l.append(l)

