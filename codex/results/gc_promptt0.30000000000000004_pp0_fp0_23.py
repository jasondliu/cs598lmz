import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This tests that gc.collect() calls tp_clear on objects that are
# collectable.  It also tests that tp_clear is called in the right
# order.

class A:
    def __del__(self):
        print "A.__del__"

class B(A):
    def __del__(self):
        print "B.__del__"
        A.__del__(self)

class C(A):
    def __del__(self):
        print "C.__del__"
        A.__del__(self)

class D(B, C):
    def __del__(self):
        print "D.__del__"
        B.__del__(self)
        C.__del__(self)

class E(D):
    def __del__(self):
        print "E.__del__"
        D.__del__(self)

a = A()
b = B()
c = C()
d = D()
e = E()

# Create
