import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a number of different types of objects.
# This is a regression test for a bug that caused collect() to run
# forever when a list with a finalizer was part of a cycle.

class A:
    pass

class B:
    pass

class C:
    pass

class D(A, B, C):
    pass

class E(A, B, C):
    pass

class F(A, B, C):
    pass

class G(A, B, C):
    pass

class H(A, B, C):
    pass

class I(A, B, C):
    pass

class J(A, B, C):
    pass

class K(A, B, C):
    pass

class L(A, B, C):
    pass

class M(A, B, C):
    pass

class N(A, B, C):
    pass

class O(A, B, C):
    pass

class P(A, B, C):
    pass

class Q(A,
