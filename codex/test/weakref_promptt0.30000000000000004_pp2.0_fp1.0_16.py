import weakref
# Test weakref.ref() with a class instance.

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
