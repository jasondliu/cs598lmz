import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an object that is a member of a
# container.  The weakref should be cleared before the container is
# destroyed.

class C:
    pass

def f():
    c = C()
    c.x = [weakref.ref(c)]
    c.y = c
    del c
    gc.collect()

f()
