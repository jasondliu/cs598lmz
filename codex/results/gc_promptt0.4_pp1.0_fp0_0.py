import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class C:
    pass

c = C()
c.x = c
del c
gc.collect()

# Test gc.garbage
gc.garbage
gc.garbage.append(1)
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append
