import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a cycle and make sure it gets collected
l = []
l.append(l)
del l
gc.collect()

# Create a cycle and make sure it gets collected, with a __del__
# method.
class A:
    def __del__(self):
        pass
a = A()
a.a = a
del a
gc.collect()

# Create a cycle and an object with a __del__ method, and a
# weakref to the object with __del__.
class B:
    def __del__(self):
        pass
b = B()
b.b = b
wr = weakref.ref(b)
del b
gc.collect()

# Test gc.garbage

# Create a cycle and an object with a __del__ method, and a
# weakref to the object with __del__.
class C:
    def __del__(self):
        pass
c = C()
c.c = c
wr = weakref.ref(c)
del c
gc.collect()
if gc.garbage
