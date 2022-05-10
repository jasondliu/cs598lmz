import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):
    pass

foo = Foo()
foo_id = id(foo)
r = weakref.ref(foo)
assert r() is foo
assert r.__call__() is foo
assert r() is not None
assert r.__call__() is not None

foo = None
assert r() is None
assert r.__call__() is None

# test weakref.proxy

class Foo(object):
    pass

foo = Foo()
foo_id = id(foo)
p = weakref.proxy(foo)
assert p is not None
assert type(p) is weakref.ProxyType
assert p is foo
assert p.__class__ is Foo
assert p.__dict__ is foo.__dict__

foo = None
try:
    p.some_attr
except ReferenceError:
    pass
else:
    raise RuntimeError

# test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
foo = Foo()
d[foo] = 'bar'
assert d
