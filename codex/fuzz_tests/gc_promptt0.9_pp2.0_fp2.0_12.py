import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() during ref counting finalizers.
class C:
    pass

w = weakref.ref(C())
del C
for i in range(100):
    gc.collect(i)

def finalize(obj):
    print("finalize", obj)
    print("       ->", obj() is not None)
    del finalize

w = weakref.finalize(C(), finalize)
gc.collect()

print("ignore me", C(), C())
gc.collect()
