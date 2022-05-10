import weakref
# Test weakref.ref()
class Foo(object):
    pass

a = Foo()

# Test weakref.proxy()
b = object.__new__(Bar)
c = weakref.proxy(b)
