import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.set_debug()

# Create a bunch of objects, and make sure gc.collect() finds them all.
# Also, make sure gc.collect() is called automatically when the test
# exits.

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

class I(object):
    pass

class J(I):
    pass

class K(I):
    pass

class L(J, K):
    pass

class M(object):
    def __del__(self):
        pass

class N(object):
    def __del__(self):
        pass

class O(N):
    def __del__(self):
        pass

class P(object):
    def __del__(self):
        pass

class Q(object
