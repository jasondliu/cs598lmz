import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
#
# This test is not very good, because it depends on the
# order in which the objects are collected.  The test
# passes if the weakref callback is called before the
# object is collected, but it fails if the object is
# collected before the callback is called.

class A:
    pass

class B:
    pass

class C:
    pass

class D:
    pass

class E:
    pass

class F:
    pass

class G:
    pass

class H:
    pass

class I:
    pass

class J:
    pass

class K:
    pass

class L:
    pass

class M:
    pass

class N:
    pass

class O:
    pass

class P:
    pass

class Q:
    pass

class R:
    pass

class S:
    pass

class T:
    pass

class U:
    pass

class V:
    pass

class W:
    pass


