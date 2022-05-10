import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

class C:
    pass

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    del a, b, c
    gc.collect()

f()
f()
f()

# Test gc.get_objects()

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    del a, b, c
    gc.collect()

f()
f()
f()

# Test gc.get_referrers()

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    del
