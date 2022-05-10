import weakref
# Test weakref.ref()

class Foo(object):
    pass

def test():
    foo = Foo()
    foo.bar = Foo()
    foo.bar.foo = foo
    foo.bar.bar = foo.bar
    foo.bar.foo2 = weakref.ref(foo)
    foo.bar.bar2 = weakref.ref(foo.bar)
    foo.bar.foo3 = weakref.proxy(foo)
    foo.bar.bar3 = weakref.proxy(foo.bar)
    foo.bar.foo4 = weakref.finalize(foo, lambda x: None)
    foo.bar.bar4 = weakref.finalize(foo.bar, lambda x: None)
    del foo
    del foo.bar

test()

# Test weakref.WeakKeyDictionary()

class Foo(object):
    pass

def test():
    foo = Foo()
    foo.bar = Foo()
    foo.bar.foo = foo
    foo.bar.bar = foo.bar
    foo.bar.foo2 = weakref.WeakKeyDictionary
