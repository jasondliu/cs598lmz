import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() not needed.
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
print "gc.collect() is not needed to collect a"
a = None
gc.collect()
print "gc.collect() is not needed to collect a"
gc.collect()

# Test gc.collect() is needed.
class A(object):
    pass

a = A()
a.b = A()
a.b.a = a
print "gc.collect() is needed to collect a"
a = None
gc.collect()
print "gc.collect() is needed to collect a"
gc.collect()

# Test gc.collect() is not needed with __del__.
class A(object):
    def __del__(self):
        pass

a = A()
a.b = A()
a.b.a = a
print "gc.collect() is not needed to collect a"
a = None
gc.collect()
print "gc.collect() is not needed to collect a"
gc.collect
