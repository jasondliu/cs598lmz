import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    c = C()
    c.x = c
    wr = weakref.ref(c)
    c = None
    gc.collect()
    assert wr() is None

f()

# Test gc.garbage

class C:
    pass

def f():
    c = C()
    c.x = c
    wr = weakref.ref(c)
    c = None
    gc.collect()
    assert wr() is None
    assert gc.garbage == []

f()

# Test gc.get_debug()

def f():
    assert gc.get_debug() == gc.DEBUG_COLLECTABLE

f()

# Test gc.get_count()

def f():
    assert gc.get_count() == (0, 0, 0)

f()

# Test gc.get_threshold()

def f():
    assert gc.get_threshold() == (700, 10, 10)


