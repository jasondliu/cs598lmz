import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.y = Foo()
f.x.y.z = f

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.collect())
print(gc.collect())

