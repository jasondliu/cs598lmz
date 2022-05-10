import weakref
# Test weakref.ref

# object to weakref
class Foo(object): pass
foo = Foo()
wr = weakref.ref(foo)
assert wr() is foo
assert weakref.getweakrefcount(foo) == 1

# callable to weakref
class CallableWithRef(object):
    __slots__ = 'x',
    def __call__(self):
        pass
wr = weakref.ref(CallableWithRef())
assert wr() is not None
# test with noncallable descriptor
try:
    weakref.ref(CallableWithRef().x)
except TypeError:
    pass
else:
    assert False, "expected a TypeError"

# builtin_function_or_method to weakref
wr = weakref.ref(len)
assert wr() is len

# method to weakref
class C(object):
    def f(self):
        pass
wr = weakref.ref(C().f)
assert wr() is not None

# callable object to weakref
wr = weakref.ref(C().f)
assert wr() is not None
