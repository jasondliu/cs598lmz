import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
#
# Test weakref.ref()
#
# Create a class with a __del__ method
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        #print '__del__ method called', self.name
        pass

# Create a Foo instance
f = Foo('f')

# Create a weakref to f
w = weakref.ref(f)

# Verify that w() returns f
assert w() is f

# Delete f
del f

# Verify that w() returns None
assert w() is None

# Verify that gc.collect() cleans up f's weakref
gc.collect()
assert len(gc.garbage) == 0

#
# Test weakref.WeakValueDictionary()
#
d = weakref.WeakValueDictionary()
d['foo'] = Foo('foo')
d['bar'] = Foo('bar')
d['baz'] = Foo('baz')

# Verify that d contains three items
assert len(d
