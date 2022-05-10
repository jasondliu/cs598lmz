import weakref
# Test weakref.ref() with a cyclic reference.
class Foo:
    pass

f = Foo()
f.f = f

wr = weakref.ref(f)
