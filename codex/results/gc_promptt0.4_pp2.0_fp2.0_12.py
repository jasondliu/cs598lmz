import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    l = [1, 2, 3]
    l2 = l
    l = None
    l2.append(4)
    return l2

def g():
    l = [1, 2, 3]
    l2 = l
    l = None
    l2.append(4)
    l2 = None
    return l2

def h():
    l = [1, 2, 3]
    l2 = l
    l = None
    l2.append(4)
    l2 = None
    l = l2
    return l

def i():
    l = [1, 2, 3]
    l2 = l
    l = None
    l2.append(4)
    l2 = None
    l = l2
    l2 = None
    return l

def j():
    l = [1, 2, 3]
    l2 = l
    l = None
    l2.append(4)
    l2 = None
    l = l2
    l2 = None
    l
