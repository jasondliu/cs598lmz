import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect twice...
for i in range(2):
    print(gc.collect())
    print(gc.collect())
    print(gc.collect())

# Test gc_collect twice...
for i in range(2):
    gc.collect()
    gc.collect()
    gc.collect()

w = weakref.ref(d['harvey'])
print(w)
print(w())

del d
print(gc.collect())
print(w)
print(w())

print(d)  # keyerror
print(gc.get_objects())
print(gc.garbage)
