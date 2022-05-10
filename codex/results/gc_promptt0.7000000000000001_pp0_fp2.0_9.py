import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectible()

# Test class.
class Foo:
    def __del__(self):
        pass

# Check that the class is collectible.
assert not gc.is_tracked(Foo)
assert gc.is_tracked(Foo())

# Check that instances are collectible.
f = Foo()
assert gc.is_tracked(f)
assert gc.get_referents(f) == [f]

# Check that weak references are collectible.
wr = weakref.ref(f)
assert gc.is_tracked(wr)
assert gc.get_referents(wr) == [wr]

# Check that weakref callbacks are collectible.
def callback(*args):
    pass
wr = weakref.ref(f, callback)
assert gc.is_tracked(wr)
assert gc.get_referents(wr) == [wr, callback]

# Check that slotted objects are collectible.
class Foo(object):
    __slots__ = ['a']
f = Foo()

