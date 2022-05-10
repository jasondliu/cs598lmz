import weakref
# Test weakref.ref() with a class instance.

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print r() is f
f = None
print r() is None
