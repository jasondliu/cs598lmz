import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on objects with finalizers, and verify that the
# finalizer is called.

class A:
    def __del__(self):
        print "A.__del__"

class B:
    def __del__(self):
        print "B.__del__"

class C(A, B):
    def __del__(self):
        print "C.__del__"
        super(C, self).__del__()

class D(C):
    def __del__(self):
        print "D.__del__"
        super(D, self).__del__()

class E(D):
    def __del__(self):
        print "E.__del__"
        super(E, self).__del__()

class F(E):
    def __del__(self):
        print "F.__del__"
        super(F, self).__del__()

class G(F):
    def __del__(self):
        print "G.__del__"
        super(G, self).__
