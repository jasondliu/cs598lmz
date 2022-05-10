import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable() being true before and false after collection

class C:
    pass

c = C()

weakref.ref(c)
gc.collect()
print(gc.collectable())
#weakref.ref(c)
#gc.collect()
#print gc.collectable()
