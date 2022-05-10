import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage

a = []
b = [a]
a.append(b)
del a
del b
gc.collect()
print(len(gc.garbage))

del gc.garbage[:]

a = []
b = [a]
a.append(b)

del gc.garbage[:]

#rf = weakref.ref(a)
#a = None
#b = None
gc.collect()
print(len(gc.garbage))
#rf()

"""
del gc.garbage[:]

a = []
b = [a]
a.append(b)
a = None
b = None
gc.collect()
print(len(gc.garbage))

del gc.garbage[:]

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()
print(len(gc.garbage))
"""

"""
del gc.garbage[:]


