import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a list of objects, and then delete the list.
# The list and the objects should be collected.

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

class X:
    pass

class Y:
    pass

class Z:
    pass

a = A()
b = B()
c = C()
d = D
