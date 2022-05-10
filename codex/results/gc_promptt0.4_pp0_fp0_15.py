import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a weakref object.
class C(object):
    pass

c = C()
r = weakref.ref(c)
assert r() is c
del c
test_support.gc_collect()
assert r() is None

# Test gc.collect() on a weakref object with a callback.
class C(object):
    pass

c = C()
r = weakref.ref(c, lambda x: None)
assert r() is c
del c
test_support.gc_collect()
assert r() is None

# Test gc.collect() on a weakref object with a callback that raises an
# exception.
class C(object):
    pass

c = C()
def callback(x):
    raise Exception
r = weakref.ref(c, callback)
assert r() is c
del c
test_support.gc_collect()
assert r() is None

# Test gc.collect() on a weakref object with a callback that raises an
# exception.
class C(object):
    pass

c = C()
def callback
