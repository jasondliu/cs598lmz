import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable() with a cycle that is broken

class Foo(object):
    __slots__ = 'x', 'y'

L = []
for i in range(10):
    a = Foo()
    a.x = 'x'
    a.y = 'y'
    L.append(a)
    L.append(weakref.ref(a))
    L.append(a)
    L.append(weakref.ref(a))
    del a

# gc will only collect the A object if it's at the end of
# the list.  This is a heuristic for dealing with lists
# that a programmer is currently changing.
gc.collect()

# Should print (2, 4)
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
