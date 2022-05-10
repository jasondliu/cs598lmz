import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
a = weakref.ref(1)
b = weakref.ref(1)
gc.collect()
assert gc.collect() == 0
del a, b
gc.collect()
assert gc.collect() == 0

# Test gc.collect() with a garbage cyclic trashcan
class A:
    def __del__(self):
        b = self.b

a = A()
a.b = a
del a
gc.collect()
assert gc.collect() == 0

# Test gc.collect() with a finalizer
class A:
    def __del__(self):
        pass

a = A()
del a
gc.collect()
assert gc.collect() == 0

# Test gc.collect() with a finalizer and a trashcan
class A:
    def __del__(self):
        b = self.b

a = A()
a.b = a
del a
gc.collect()
assert gc.collect() == 0

# Test gc.collect() with a finalizer and
