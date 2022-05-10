import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a list of objects to be collected
class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

a = A('a')
b = A('b')
c = A('c')
d = A('d')
e = A('e')
f = A('f')
g = A('g')
h = A('h')
i = A('i')
j = A('j')
l = [a, b, c, d, e, f, g, h, i, j]

# Create a list of references to those objects
r = []
for o in l:
    r.append(weakref.ref(o))

# Delete the original list of objects
del l

# Collect
gc.collect()

# Print the list of weak references
print(r)

# Print the objects that are still alive
for o in r:
    print(o())

# Create a cycle
a = A('a
