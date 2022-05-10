import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        print "A.__del__"

class B:
    def __del__(self):
        print "B.__del__"

class C:
    def __del__(self):
        print "C.__del__"

class D:
    def __del__(self):
        print "D.__del__"

class E:
    def __del__(self):
        print "E.__del__"

class F:
    def __del__(self):
        print "F.__del__"

class G:
    def __del__(self):
        print "G.__del__"

class H:
    def __del__(self):
        print "H.__del__"

class I:
    def __del__(self):
        print "I.__del__"

class J:
    def __del__(self):
        print "J.__del__"

class K:
    def __del__(self):

