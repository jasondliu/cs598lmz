import weakref
# Test weakref.ref

class Foo(object):
    pass

def test():
    f = Foo()
    ref = weakref.ref(f)
    assert ref() is f
    del f
    assert ref() is None

test()
print('passed')
