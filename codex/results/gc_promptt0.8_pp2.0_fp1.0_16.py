import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
s = gc.collect()
print s
print

# Test gc.get_referents
a = []
b = [a, a]
c = [a, b]
d = [c, b]
del a, b, c, d
print gc.get_referents(None)
print

# Test gc.get_referrers
a = []
b = [a, a]
c = [a, b]
d = [c, b]
print gc.get_referrers(*gc.get_referents(a))
print

# Test gc.get_objects
print len(gc.get_objects())
print

# Test gc.get_count
print gc.get_count()
print

# Test gc.get_stats
print gc.get_stats()
print

# Test gc.garbage
print len(gc.garbage)
print

# Test gc.get_referrers as a function
x = []
y = [x, [x], dict(x
