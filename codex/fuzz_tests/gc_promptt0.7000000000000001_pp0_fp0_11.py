import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a chain of weakrefs.
# This chain was reported to leak in 2.2.
class C(object):
    pass
a = C()
b = C()
a.b = b
b.a = a
a.w = weakref.ref(a)
b.w = weakref.ref(b)
print gc.collect()
# Test gc.collect() with a cycle of old-style classes.
# This cycle was reported to leak in 2.2.
class C:
    pass
a = C()
b = C()
a.b = b
b.a = a
print gc.collect()
# Test gc.collect() with a cycle of objects with __del__ methods.
# This cycle was reported to leak in 2.2.
class C(object):
    def __del__(self):
        pass
a = C()
b = C()
a.b = b
b.a = a
print gc.collect()
# Test gc.collect() with a cycle of objects with __del__ methods
# that invoke gc.collect
