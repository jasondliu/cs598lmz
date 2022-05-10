import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

print('gc.garbage:', gc.garbage)
print('gc.collect():', gc.collect())
print('gc.garbage:', gc.garbage)

# Test weakrefs

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

a = A('a')
b = A('b')
c = A('c')
w = weakref.ref(a)
gc.collect()
print('gc.garbage:', gc.garbage)
print('w():', w())
a = None
gc.collect()
print('gc.garbage:', gc.garbage)
print('w():', w())
gc.garbage.append(b)
gc.garbage.append(c)
gc.collect()
print('gc.garbage:', gc.garbage)

# Test finalizers

class B:
    def __init__(self, name):
        self
