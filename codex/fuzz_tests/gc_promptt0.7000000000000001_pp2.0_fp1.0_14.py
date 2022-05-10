import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

o = C()
r = weakref.ref(o)

# gc.collect()
for i in range(2):
    print(gc.collect())

del o
print(gc.collect())
print(r())

print('end')
