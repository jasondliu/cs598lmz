import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()'s collection of cyclic trash which is
# part of a cycle with a global.  This is the first of two tests.
# The second is in test_gc.
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)

class A:
    pass

class B(A):
    pass

a = A()
b = B()

a.other = b
b.other = a

wr = weakref.ref(a)

del a, b

gc.collect()
gc.collect()
gc.collect()

class C(object):
    pass

class D(C):
    pass

c = C()
d = D()

c.other = d
d.other = c

wr = weakref.ref(c)

del c, d

gc.collect()
gc.collect()
gc.collect()
import gc

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):

