import weakref
# Test weakref.ref()

class Foo(object):
    pass

def test():
    f = Foo()
    r = weakref.ref(f)
    print(r())
    print(r() is f)
    print(r() is None)
    print(r() is None)
    print(r() is None)
    print(r() is None)

test()
