import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
