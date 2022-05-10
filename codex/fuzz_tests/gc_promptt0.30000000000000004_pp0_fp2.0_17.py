import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This test is a bit tricky.  It's hard to test that gc.collect()
# actually collects something, because the collector is too fast.
# So, we have to create some objects and make sure that they go away.
# We do that by creating a bunch of cycles and then deleting references
# to the objects in the cycles.  If we can convince the collector that
# those objects are uncollectable, then we'll be able to trigger the
# bug.

# Create a bunch of objects, and make them part of cycles.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    pass

class F(E):
    pass

class G(E):
    pass

class H(F, G):
    pass

class I(D, H):
    pass

class J:
    pass

class K(J):
    pass

class L(J):
    pass

class M(K, L):
    pass
