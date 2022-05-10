import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
import gc
import weakref

class A(object):
    pass

class B(object):
    pass

a = A()
a.b = B()
del a.b

a = B()
b = A()
b.a = a
del a

b = A()
a = B()
b.a = a
b = None

# del a
gc.collect()

# Test gc.get_objects
import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
objects = gc.get_objects()
assert len(objects) > 1

# Test gc.get_objects filter false
import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
objects = gc.get_objects(False)
# fill up gc with unreachable objects
referrers = {}
for i in xrange(100):
    a   = []
    b   = A()
    id  = id(a)
    a.append(b)
    # Make this object not only unreachable but
