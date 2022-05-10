import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a custom __del__ method.
class A:
    def __del__(self):
        pass

a = A()
a_id = id(a)
del a
gc.collect()
print gc.garbage
assert a_id not in gc.garbage

class A:
    def __del__(self):
        pass

a = A()
a_id = id(a)
del a
gc.collect()
print gc.garbage
assert a_id in gc.garbage

# Test gc.collect() with a custom __del__ method and a cyclic reference.
class A:
    def __del__(self):
        pass

a = A()
a.a = a
a_id = id(a)
del a
gc.collect()
print gc.garbage
assert a_id not in gc.garbage

class A:
    def __del__(self):
        pass

a = A()
a.a = a
a_id = id(a)
del a
gc.
