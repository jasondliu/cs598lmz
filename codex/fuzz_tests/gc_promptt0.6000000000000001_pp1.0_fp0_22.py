import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a class instance

class Test:
    pass

t = Test()
w = weakref.ref(t)

print(gc.collect())
print(gc.collect())
print(w())
print(gc.collect())
print(w())
t = None
print(gc.collect())
print(w())
print(gc.collect())
print(w())
