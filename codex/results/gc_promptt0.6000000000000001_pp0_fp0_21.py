import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
#
# Create a bunch of objects, then collect.  Ensure that the
# collector finds everything.

class C:
    pass

def f():
    l = []
    for i in range(100):
        c = C()
        l.append(c)
    del l

def g():
    l = []
    for i in range(100):
        c = C()
        l.append(c)
    del l
    weakref.ref(C)

def h():
    l = []
    for i in range(100):
        c = C()
        l.append(c)
    del l
    weakref.ref(C)
    gc.collect()

def test():
    f()
    g()
    h()
    gc.collect()

test()
