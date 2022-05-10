import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that raises an error.

def callback(w):
    raise Exception

class A:
    pass

a = A()
w = weakref.ref(a, callback)

del a
gc.collect()
# Test cyclic gc.collect() with a weakref callback that raises an error.

def callback(w):
    raise Exception

class A:
    pass

a = A()
w = weakref.ref(a, callback)
b = A()
a.b = b
b.a = a

del a, b
gc.collect()
# Tests gc.garbage:
#   - cyclic objects
#   - objects with __del__
#   - objects with __del__ and __getattr__

# Create cyclic objects with __del__, and make sure they are in gc.garbage

gc.garbage[:] = []
class A:
    def __del__(self):
        pass
class B:
    def __del__(self):
        pass
class C:
    def __del
