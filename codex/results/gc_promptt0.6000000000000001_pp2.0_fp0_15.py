import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
# Test that gc.collectable() doesn't crash in case of a non-collectable
# object.

def f():
    l = []
    l.append(l)
    return l

x = f()
print(gc.is_tracked(x))
print(gc.is_tracked(x[0]))
print(gc.collectable(x))
print(gc.collectable(x[0]))

# Test that gc.collectable() doesn't crash in case of a non-collectable
# object.

def f():
    return weakref.ref(object())

x = f()
print(gc.is_tracked(x))
print(gc.collectable(x))

# Test that gc.collectable() doesn't crash in case of an array of
# non-collectable objects.

def f():
    return [object(), object()]

x = f()
print(gc.is_tracked(x))
print(gc.collectable(x))

# Test that gc.collectable()
