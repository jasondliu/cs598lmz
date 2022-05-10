import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in a low-memory situation
import sys
r = weakref.ref(sys)
try:
    import sys
    assert sys is r()
    del sys
    gc.collect()
    assert r() is None
finally:
    del r

def callback(r):
    print 'callback', r

class A:
    pass

a = A()
r = weakref.ref(a, callback)

# Check that the reference is not dead
assert r() is a
del a

# Check the callback
gc.collect()
del r

# Check that the callback has been called
gc.collect()

# Check weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
d[1] = a = A()
d[2] = a

# Check that the values are there
assert len(d) == 2
assert a in d.values()

# Check that the keys are there
assert 1 in d
assert 2 in d

# Check that the object has not been deleted
assert a is d[1]
assert a is
