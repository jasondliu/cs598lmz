import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The test verifies that all objects are correctly collected.
#
# This test is supposed to be run with the -R option.

class X:
    pass

def f():
    x = X()
    x.a = x
    x.b = X()
    x.b.a = x
    x.b.b = x.b
    del x

def g():
    x = X()
    x.a = x
    x.b = X()
    x.b.a = x
    x.b.b = x.b
    return weakref.ref(x)

def h():
    x = X()
    x.a = x
    x.b = X()
    x.b.a = x
    x.b.b = x.b
    return weakref.ref(x.b)

f()
gc.collect()

r = g()
gc.collect()

s = h()
gc.collect()

del r, s
gc.collect()

# This should have collected everything
