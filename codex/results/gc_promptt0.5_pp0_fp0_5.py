import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a destructor that does nothing.
class A(object):
    def __del__(self):
        pass

# Create a cycle.
a = A()
a.b = a

# Create a second cycle.
a = A()
a.b = a

# Create a third cycle.
a = A()
a.b = a

# Create a fourth cycle.
a = A()
a.b = a

# Create a fifth cycle.
a = A()
a.b = a

# Create a sixth cycle.
a = A()
a.b = a

# Create a seventh cycle.
a = A()
a.b = a

# Create an eighth cycle.
a = A()
a.b = a

# Create a ninth cycle.
a = A()
a.b = a

# Create a tenth cycle.
a = A()
a.b = a

# Create an eleventh cycle.
a = A()
a.b = a

# Create a twelfth cycle.
a = A()
a.b =
