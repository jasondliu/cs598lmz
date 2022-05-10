import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a cyclic garbage object

class A:
    pass

a = A()
a.b = A()
a.b.a = a

a_id = id(a)

#
# Check that the object is in the cyclic garbage
del a
gc.collect()

objs = gc.garbage

if len(objs) != 1:
    raise TestFailed, "expected one object in gc.garbage, found %d" % len(objs)

if id(objs[0]) != a_id:
    raise TestFailed, "expected object in gc.garbage to be a"

#
# Check that the object is still in the cyclic garbage
gc.garbage[:] = []
gc.collect()

objs = gc.garbage

if len(objs) != 1:
    raise TestFailed, "expected one object in gc.garbage, found %d" % len(objs)

if id(objs[0]) != a_id:
    raise TestFailed, "
