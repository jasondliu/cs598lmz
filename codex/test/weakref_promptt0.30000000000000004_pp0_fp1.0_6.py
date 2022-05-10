import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
