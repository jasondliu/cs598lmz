import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    s = 'abc'
    t = (s, s)
    del s
    return t

def g():
    s = 'abc'
    t = (s, s)
    del s
    gc.collect()
    return t

def h():
    s = 'abc'
    t = (s, s)
    del s
    return weakref.ref(t)

def i():
    s = 'abc'
    t = (s, s)
    del s
    gc.collect()
    return weakref.ref(t)

def j():
    s = 'abc'
    t = (s, s)
    del s
    gc.collect()
    return weakref.ref(t)()

print(gc.collect())
print(gc.collect())
print(gc.collect())

t = f()
print(gc.collect())
print(gc.collect())
print(gc.collect())
del t
print(gc.collect())
print(gc.collect())
print(gc
