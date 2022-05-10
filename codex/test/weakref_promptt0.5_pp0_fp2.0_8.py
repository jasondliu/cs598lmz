import weakref
# Test weakref.ref()
class Foo(object):
    pass

f = Foo()

# Create a weak reference to f
f_ref = weakref.ref(f)
