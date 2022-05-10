import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on objects with custom tp_dealloc functions.

class C:
    def __del__(self):
        print "C.__del__"

class D(C):
    def __del__(self):
        print "D.__del__"
        C.__del__(self)

class E(C):
    def __del__(self):
        print "E.__del__"
        C.__del__(self)

class F(C):
    def __del__(self):
        print "F.__del__"
        C.__del__(self)

class G:
    def __del__(self):
        print "G.__del__"

class H(G):
    def __del__(self):
        print "H.__del__"
        G.__del__(self)

class I(G):
    def __del__(self):
        print "I.__del__"
        G.__del__(self)

class J(G):
    def __del__(self
