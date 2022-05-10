import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo(object):
    pass

obj = Foo()

def test(obj):
    r1 = weakref.ref(obj)
    r2 = weakref.ref(obj)
