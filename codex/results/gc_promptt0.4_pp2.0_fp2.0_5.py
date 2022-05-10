import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

a = A()
a.b = B()

w = weakref.ref(a)

del a

gc.collect()

print w() is None

# Test gc.get_referrers()

class C:
    pass

c = C()

l = [c]

d = {}
d[1] = c

s = set([c])

gc.collect()

print gc.get_referrers(c) == [l, d, s]

# Test gc.get_referents()

print gc.get_referents(l) == [c]
print gc.get_referents(d) == [c]
print gc.get_referents(s) == [c]

# Test gc.get_objects()

print c in gc.get_objects()
print l in gc.get_objects()
print d in gc.get_objects()
print s in g
