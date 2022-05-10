import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class Foo:
    pass

def bar():
    pass

f = Foo()
b = bar
del Foo, bar

print(gc.collectable(f))
print(gc.collectable(b))

print(gc.collect())

print(gc.collectable(f))
print(gc.collectable(b))

print(gc.collect())

print(gc.collectable(f))
print(gc.collectable(b))

f = None
b = None

print(gc.collect())

print(gc.collectable(f))
print(gc.collectable(b))

print(gc.collect())

print(gc.collectable(f))
print(gc.collectable(b))

# Test gc.get_referrers()

class Foo:
    pass

def bar():
    pass

f = Foo()
b = bar
del Foo, bar

print(gc.get_referrers(f))
print(gc.get_referrers(b))

print(gc
