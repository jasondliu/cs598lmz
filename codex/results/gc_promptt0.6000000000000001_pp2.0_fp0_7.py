import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
# Create a cycle and make sure it gets collected.
l = []
l.append(l)
del l
gc.collect()
gc.collect()
# Create a reachable object with a __del__ method, and make sure it
# gets collected.
class A:
    def __del__(self):
        pass
a = A()
del a
gc.collect()
gc.collect()
# Create a reachable object with a __del__ method that raises an
# exception.  Make sure the exception doesn't prevent collection of
# the object.
class B:
    def __del__(self):
        raise Exception
b = B()
del b
gc.collect()
gc.collect()
# Create a reachable cycle.
class C:
    def __init__(self, other):
        self.other = other
c = C(None)
c.other = c
del c
gc.collect()
gc.collect()
# Create a reachable cycle with a __del__ method.
class D:
    def __init__(self, other):

