import weakref
# Test weakref.ref(f())
# class Foo(object): pass
# def f(): return Foo()
# wr = weakref.ref(f())
# assert wr() is not None

# Test weakref as decorator.
def decorator(func):
    r = weakref.ref(func)
    assert r() is not None
    return 'decoration %s' % r().__name__

@decorator
def foo():
    pass
assert isinstance(foo, str)

# Test weakref.proxy()
class A(object): pass
