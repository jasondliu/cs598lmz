import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
collectable = []
removed = []
def remove(ref):
    removed.append(ref)
def callback(ignore):
    collectable.append(weakref.ref(A(), remove))
a = A()
callback(a)
assert collectable[0]() is a
a = None
assert len(collectable) == 1
assert len(removed) == 0
gc.collect()
assert len(collectable) == 1
assert len(removed) == 0
del collectable[0]
gc.collect()
assert len(collectable) == 0
assert len(removed) == 1
assert removed[0]() is None

# Test gc.garbage
class A:
    def __del__(self):
        gc.garbage.append(self)
gc.garbage[:] = []
a = A()
del a
assert not gc.garbage
gc.collect()
assert len(gc.garbage) == 1
del gc.garbage[0]
gc.collect()
assert not gc.garbage

# Test gc
