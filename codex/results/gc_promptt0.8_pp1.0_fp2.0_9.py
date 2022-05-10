import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
x = weakref.ref(gc.collectable())
# Test gc.get_referrers() - this test may fail if the call to get_referrers()
# is optimized away
a = [1,2,3]
b = [a, a[:], a[:]]
literals = gc.get_referrers(*a)
assert b in literals
# Test gc.get_referrers(object, ...)
# The test may fail if the call to get_referrers() is optimized away
def f():
    b = f
    literals = gc.get_referrers(*b.__code__.co_consts)
    assert f in literals
f()
# Test gc.get_referrers(object, ...) - this test may fail if the call to
# get_referrers() is optimized away
def f():
    b = f
    literals = gc.get_referrers(*b.__code__.co_consts)
    assert f in literals
f()
# Test g
