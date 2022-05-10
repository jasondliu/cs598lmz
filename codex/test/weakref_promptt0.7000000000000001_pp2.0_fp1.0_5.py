import weakref
# Test weakref.ref with a bound method.

class Foo:

    def __init__(self):
        self.bar = 'bar'

    def __del__(self):
        pass

    def foo(self):
        pass


f = Foo()
f2 = weakref.ref(f.foo)
