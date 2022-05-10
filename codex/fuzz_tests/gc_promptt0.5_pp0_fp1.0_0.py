import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

c = C()
wr = weakref.ref(c)

del c
print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.collect())
print(wr())

print(gc.
