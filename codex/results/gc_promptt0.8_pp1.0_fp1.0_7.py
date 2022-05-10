import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

# D has __del__.
# A, B and C don't.

def test():
    class D(B, C):
        def __del__(self):
            pass

    b = B()
    c = C()
    d = D()

    weakrefs = [
        weakref.ref(B),
        weakref.ref(C),
        weakref.ref(D),
        weakref.ref(b),
        weakref.ref(c),
        weakref.ref(d),
    ]

    del b, c, d
    gc.collect()

    for w in weakrefs:
        assert w() is not None, "Weak reference wasn't cleared"

    # Pass

test()
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A
