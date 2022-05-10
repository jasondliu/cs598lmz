import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a cyclic reference to a tuple
def create_cycle():
    l = [1, 2, 3]
    l.append(l)
    return l

def create_cycle2():
    t = (1, 2, 3)
    t = t, t
    return t

def create_cycle3():
    t = (1, 2, 3)
    t = t, t
    return t

def create_cycle4():
    t = (1, 2, 3)
    t = t, t
    return t

def create_cycle5():
    t = (1, 2, 3)
    t = t, t
    return t

def create_cycle6():
    t = (1, 2, 3)
    t = t, t
    return t

def create_cycle7():
    t = (1, 2, 3)
    t = t, t
    return t

def create_cycle8():
    t = (1, 2, 3)
    t = t, t
    return t

def create
