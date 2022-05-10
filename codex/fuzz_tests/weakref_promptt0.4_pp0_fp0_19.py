import weakref
# Test weakref.ref() on a class instance.
import gc

class C(object):
    pass

c = C()
r = weakref.ref(c)
print r() is c
del c
print r() is None
gc.collect()
print r() is None

# Test weakref.ref() on a list.
l = []
r = weakref.ref(l)
print r() is l
del l
print r() is None
gc.collect()
print r() is None

# Test weakref.ref() on a dict.
d = {}
r = weakref.ref(d)
print r() is d
del d
print r() is None
gc.collect()
print r() is None

# Test weakref.ref() on a tuple.
t = ()
r = weakref.ref(t)
print r() is t
del t
print r() is None
gc.collect()
print r() is None

# Test weakref.ref() on a set.
s = set()
r = weakref.ref(s)
print r() is s
