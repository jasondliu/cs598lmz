import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

class B:
    pass

class C:
    pass

def callback(wr):
    print 'callback', wr

def test():
    a = A()
    b = B()
    c = C()
    a.b = b
    a.c = c
    b.a = a
    b.c = c
    c.a = a
    c.b = b
    wr = weakref.ref(a, callback)
    wr1 = weakref.ref(a)
    wr2 = weakref.ref(b)
    wr3 = weakref.ref(c)
    del a, b, c
    gc.collect()
    print wr, wr1, wr2, wr3
    print wr(), wr1(), wr2(), wr3()

test()
