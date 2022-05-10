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
print weakref.proxy(A())
a1 = A()
a2 = A()
a3 = A()
rp1 = weakref.proxy(a1)
rp2 = weakref.proxy(a2)
rp3 = weakref.proxy(a3)
assert rp1 == a1
assert rp2 == a2
assert rp3 == a3
assert rp1 != rp2 != rp3
wr1 = weakref.ref(a1)
wr2 = weakref.ref(a2)

