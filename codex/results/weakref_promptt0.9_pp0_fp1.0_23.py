import weakref
# Test weakref.ref() argument
print weakref.ref(None)
print weakref.ref(3)
print weakref.ref('abc')
print weakref.ref(3.25)
print weakref.ref(weakref)

# Make sure it's really a weak reference
import gc
class Foo(object):
    pass
f = Foo()
r = weakref.ref(f)
print r() is f # The object is still around
del f         # Remove the one reference
gc.collect()  # Run garbage collection right away
print r() is f # r() now returns None


# Test the callback mechanism
class Foo(object):
    pass
f = Foo()
def callback(r):
    print 'callback called with', r
r = weakref.ref(f, callback)
del f
gc.collect()  # Run garbage collection right away
