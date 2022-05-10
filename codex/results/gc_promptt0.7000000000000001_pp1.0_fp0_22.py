import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable().
class Foo(object):
    pass
foo = Foo()
a = weakref.ref(foo)
assert gc.is_tracked(foo)
assert not gc.is_tracked(a)
assert gc.get_referents(foo) is not None
assert gc.get_referents(a) is None
# Test gc.collectable() with a non-empty weakref.
class Foo(object):
    pass
foo = Foo()
a = weakref.ref(foo)
bar = Foo()
assert gc.is_tracked(foo)
assert gc.get_referents(foo) is not None
# Test gc.collectable() with an empty weakref.
class Foo(object):
    pass
foo = Foo()
a = weakref.ref(foo)
bar = Foo()
del foo
assert not gc.is_tracked(foo)
assert gc.get_referents(foo) is None
# Test gc.collectable() with a weakref to an object that has a weakref to itself.
