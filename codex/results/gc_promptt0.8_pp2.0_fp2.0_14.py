import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() immediately after setting gc_debug().
# This was broken in 2.3.4.
gc.collect()

class C:
    def __del__(self):
        gc.collect()

def f():
    x = C()
    x.foo = x

c = C()
c.foo = c
c_id = id(c)
c_ref = weakref.ref(c)
c = None
gc.collect()
assert c_ref() is not None
w = c_ref()
w.foo = w
c_id = None
gc.collect()

# Verify that we run __del__ methods at the end of a cycle,
# even when the cycle also involves a directly cyclic gc.
class C:
    def __init__(self, should_raise=False):
        self.should_raise = should_raise
    def __del__(self):
        if self.should_raise:
            raise RuntimeError

def f(should_raise=False):
    c = C(should_raise)
    c.foo = c

