import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

def test_collect():
    # Create a cycle
    a = A()
    a.b = B()
    a.b.a = a

    # Create a second cycle
    c = C()
    c.d = D()
    c.d.c = c

    # Break the cycle
    a = None
    c = None

    # Collect
    gc.collect()

# Test gc.get_referrers()

def test_get_referrers():
    # Create a cycle
    a = A()
    a.b = B()
    a.b.a = a

    # Create a second cycle
    c = C()
    c.d = D()
    c.d.c = c

    # Break the cycle
    a = None
    c = None

    # Collect
    gc.collect()

    # Get referrers
    r = g
