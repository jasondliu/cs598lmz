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
print repr(f2)
print f2()
print f2() is f.foo
del f
print gc.collect()
print f2()
print repr(f2)
