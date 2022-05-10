import weakref
# Test weakref.ref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def f():
    foo = Foo('bar')
    foo_ref = weakref.ref(foo)
    del foo
    return foo_ref

foo_ref = f()
