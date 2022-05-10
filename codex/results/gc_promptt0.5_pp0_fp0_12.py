import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref
class TestClass:
    pass

t = TestClass()
w = weakref.ref(t)
del t
gc.collect()

# Test gc.garbage
gc.garbage.append(t)
gc.garbage.append("test")
gc.collect()
print(gc.garbage)

print("OK")
