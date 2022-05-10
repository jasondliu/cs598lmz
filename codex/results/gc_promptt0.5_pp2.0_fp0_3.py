import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Check that no objects were collected
assert gc.collect() == 0

# Create a cycle and make sure it gets collected
l = []
l.append(l)
del l
gc.collect()
assert gc.collect() == 1

# Create a cycle and an object with a finalizer; check that
# the cycle is collected before the finalizer runs
import sys

class A:
    def __del__(self):
        global gotit
        gotit = 1

a = A()
a.x = a
del a
gc.collect()
assert gc.collect() == 1
assert gotit

# Create a cycle involving a dict
# Check that it gets collected
d = {}
d[0] = d
del d
gc.collect()
assert gc.collect() == 1

# Create a cycle involving a dict and a finalizer
# Check that the finalizer runs before the cycle is collected
class A:
    def __del__(self):
        global gotit
        gotit = 1

a = A()
d = {}
