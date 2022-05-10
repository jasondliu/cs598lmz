import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref
class MyClass:
    pass
x = MyClass()
x_id = id(x)
y = weakref.ref(x)
assert y() is x
x = None
assert gc.collect() == 1
assert y() is None
assert gc.collect() == 0

# Test weakref.WeakKeyDictionary
class MyClass:
    pass
x = MyClass()
x_id = id(x)
d = weakref.WeakKeyDictionary()
d[x] = 42
assert d[x] == 42
x = None
assert gc.collect() == 1
assert d == {}
assert gc.collect() == 0

# Test weakref.WeakValueDictionary
class MyClass:
    pass
x = MyClass()
x_id = id(x)
d = weakref.WeakValueDictionary()
d[42] = x
assert d[42] is x
x = None
assert gc.collect() == 1
assert d == {}
assert gc.collect() == 0
