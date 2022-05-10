import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a cyclic trash, but with a cycle
# length > 2.  The weakref must be cleared.

class C:
    pass

def f():
    c1 = C()
    c2 = C()
    c1.x = c2
    c2.x = c1
    wr = weakref.ref(c1)
    gc.collect()
    return wr

wr = f()
c1 = wr()
if c1 is not None:
    print("c1 still alive", c1.x.x.x.x.x.x.x.x)
    assert 0

print("ok")
