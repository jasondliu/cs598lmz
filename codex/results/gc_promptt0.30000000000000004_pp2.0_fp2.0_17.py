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

# Test weakref.ref()

class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    r = weakref.ref(a)
    del a
    gc.collect()
    print r()

f()

# Test weakref.proxy()

class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    p = weakref.proxy(a)
    del a
    gc.collect()
    print p.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a.b.a
