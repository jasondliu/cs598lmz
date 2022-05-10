import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The following test is fragile, but the best I can do.  The
# problem is that I don't know what the garbage collector will
# collect.  I've done my best to make sure that the garbage
# collector will collect the objects I create, and if it doesn't
# then the test fails.
#
# The only real way to test this is to examine the garbage
# collector's source code and make sure that the objects I've
# created will be collected.

# Create some objects that should be collectable.

class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(C, B):
    pass

class E:
    pass

class F(E):
    pass

class G(F):
    pass

class H(F, G):
    pass

class I(E):
    pass

class J(I):
    pass

class K(I, J):
    pass

class L(K):
    pass

class M(K, L):
    pass
