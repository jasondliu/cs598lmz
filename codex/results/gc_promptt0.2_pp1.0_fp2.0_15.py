import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    del a
    gc.collect()

f()

# Test gc.get_objects()
class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    del a
    gc.collect()

f()

# Test gc.get_referrers()
class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    del a
    gc.collect()

f()

# Test gc.get_referents()
class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    del a
    gc.collect()

f()

# Test gc.is_tracked()
class A:

