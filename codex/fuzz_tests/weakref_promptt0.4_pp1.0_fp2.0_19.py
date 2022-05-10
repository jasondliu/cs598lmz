import weakref
# Test weakref.ref(obj)

class Foo(object): pass

foo = Foo()
foo.bar = Foo()

def f():
    print foo.bar

def g():
    print foo

foo.bar.baz = f
foo.bar.qux = g

foo.bar.baz()
foo.bar.qux()

foo.bar.baz = weakref.ref(foo.bar)
foo.bar.qux = weakref.ref(foo)

foo.bar.baz()
foo.bar.qux()

foo.bar.baz = weakref.ref(foo.bar.baz)
foo.bar.qux = weakref.ref(foo.bar.qux)

foo.bar.baz()
foo.bar.qux()

foo.bar.baz = weakref.ref(foo.bar.baz())
foo.bar.qux = weakref.ref(foo.bar.qux())

foo.bar.baz()
foo.bar.qux()

foo.bar.baz =
