import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class A:
    pass
a = A()
del a
class B:
    pass
b = B()
b_ref = weakref.ref(b)
del b
if gc.collect():
    print "gc.collect() returns non-zero"
if b_ref():
    print "b_ref() is not None"
gc.collect()
# Test gc.DEBUG_UNCOLLECTABLE
class C:
    pass
c = C()
c_ref = weakref.ref(c)
del c
if gc.collect():
    print "gc.collect() returns non-zero"
if c_ref():
    print "c_ref() is not None"
gc.collect()
# Test gc.DEBUG_SAVEALL
gc.set_debug(gc.DEBUG_SAVEALL)
class D:
    pass
d = D()
d_ref = weakref.ref(d)
del d
d_ref2 = weakref.ref(d)
if gc.collect():
    print "gc.collect() returns non-zero"
if
