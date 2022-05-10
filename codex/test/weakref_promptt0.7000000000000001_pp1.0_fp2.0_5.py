import weakref
# Test weakref.ref() can be applied to a class instance.

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)

