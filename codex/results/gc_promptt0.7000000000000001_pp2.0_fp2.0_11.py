import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# collect() doesn't finalize weakref objects:
# See issue #6014

class C(object):
    pass

c = C()

w = weakref.ref(c)

c.attr = c
del c

gc.collect()

# Issue #23300: collector does not finalize weakref objects
# if the referent is a cycle.

class A(object):
    pass

a = A()

w1 = weakref.ref(a)

a.attr = a

del a

gc.collect()

w1()

# Issue #23300: collector does not finalize deallocated weakref objects
# if the referent is a cycle.

class B(object):
    pass

b = B()

w2 = weakref.ref(b)

b.attr = b

del b
del w2

gc.collect()

# Issue #23300: collector does not finalize weakref objects
# if the referent is a cycle.

class D(object):
