import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class X:
    pass

class Y:
    pass

x = X()
y = Y()
x.next = y
y.prev = x
del x, y
gc.collect()
assert gc.collectable() == []

x = X()
y = Y()
x.next = y
y.prev = x
del x
gc.collect()
assert gc.collectable() == [y]

x = X()
y = Y()
x.next = y
y.prev = x
del y
gc.collect()
assert gc.collectable() == [x]

x = X()
y = Y()
x.next = y
y.prev = x
del x, y
gc.collect()
assert gc.collectable() == []

x = X()
y = Y()
x.next = y
y.prev = x
del x
gc.collect()
assert gc.collectable() == [y]

x = X()
y = Y()
x.next = y
y.prev = x
