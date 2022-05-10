fn = lambda: None
# Test fn.__code__ is None
assert hasattr(fn, '__code__')
assert fn.__code__ is None
# Test fn.__code__ is not None
fn.__code__ = 'foo'
assert hasattr(fn, '__code__')
assert fn.__code__ == 'foo'
# Test fn.__code__ is not None on the class, but None on an instance
class Foo():
    pass
Foo.__code__ = 'foo'

f = Foo()
f.__code__ = None

assert f.__code__ is None
assert Foo.__code__ == 'foo'
# Test fn.__code__ is not None on the class and not None on an instance
class Foo():
    pass
class Bar(Foo):
    pass
Foo.__code__ = 'foo'
Bar.__code__ = 'bar'

f = Foo()
f.__code__ = 'foofoo'

b = Bar()
b.__code__ = 'barbar'

assert f.__code__ == 'foofoo'
assert Foo.__code__ ==
