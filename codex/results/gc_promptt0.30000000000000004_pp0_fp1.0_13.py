import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a bunch of objects, and make sure they are all collectable.

# Create a list of objects, and append to it.
l = []
for i in range(10):
    l.append(str(i) * 100)

# Create a dict of objects, and incrementally add to it.
d = {}
for i in range(10):
    d[i] = str(i) * 100

# Create a bunch of tuples
for i in range(10):
    (i,)

# Create a bunch of functions
def f(x):
    return x
for i in range(10):
    f(i)

# Create a bunch of classes
class C:
    def __init__(self, x):
        self.x = x
for i in range(10):
    C(i)

# Create a bunch of instances
for i in range(10):
    C(i)()

# Create a bunch of methods
class D:
    def f(self, x):
        return x
for i in range(10):
   
