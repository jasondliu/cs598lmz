import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return '<Foo %s>' % self.value

def test_weakref_callback(ref):
    print('callback', ref)

def test_weakref():
    foo = Foo(42)
    ref = weakref.ref(foo, test_weakref_callback)
    print(ref)
    print(ref())
    print('deleting foo')
    del foo
    print(ref)
    print(ref())

test_weakref()
