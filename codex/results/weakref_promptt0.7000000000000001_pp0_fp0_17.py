import weakref
# Test weakref.ref


class MyClass(object):
    pass


mc = MyClass()
wr = weakref.ref(mc)
assert wr() is mc

assert wr.__hash__() == weakref.ref.__hash__(wr)

# test weakref.ref is weak

del mc
assert wr() is None

# test weakref.ref is unhashable
try:
    hash(wr)
except TypeError:
    pass
else:
    assert False

# Test weakref.proxy

class MyClass(object):
    pass

mc = MyClass()
wp = weakref.proxy(mc)
assert wp is mc

# test weakref.proxy is weak

del mc
try:
    wp.foo
except ReferenceError:
    pass
else:
    assert False

# test weakref.proxy is hashable
# XXX: does this match CPython?
assert hash(wp) == hash(id(wp.__weakref__()))

# test weakref.proxy is almost an instance of the original class
assert type(wp) is My
