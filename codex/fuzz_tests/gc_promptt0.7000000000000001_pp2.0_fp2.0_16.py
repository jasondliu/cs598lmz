import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
gc.collect() # No objects found.  We created no objects, so no garbage either.
assert not gc.garbage, "No garbage should have been found"

# Create some objects and show there are no references to them
def func():
    x = 42
    x = 'this is a string'
    x = [1, 2, 3, 4]
func()
gc.collect()
assert not gc.garbage, "No garbage should have been found"

# Create some objects and show there are no references to them
class A:
    pass
x = A()
y = A()
del x
del y
gc.collect()
assert not gc.garbage, "No garbage should have been found"

# Create some objects and show there are no references to them
gc.collect()
assert not gc.garbage, "No garbage should have been found"

# Create some objects and show there are no references to them
class A:
    pass
x = A()
y = A()
del x
del y
gc.collect()
assert
