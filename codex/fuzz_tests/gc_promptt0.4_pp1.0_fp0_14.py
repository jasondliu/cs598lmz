import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

def f(x):
    pass

a = A()
w = weakref.ref(a)
f(a)
a = None
gc.collect()
print(w(), w())

gc.collect()
print(w(), w())

# Test gc.garbage

class A:
    pass

def f(x):
    pass

a = A()
w = weakref.ref(a)
f(a)
a = None
gc.collect()
print(gc.garbage)

# Test gc.get_debug()

print(gc.get_debug())

# Test gc.get_count()

print(gc.get_count())

# Test gc.get_objects()

print(len(gc.get_objects()))

# Test gc.get_referrers()

print(len(gc.get_referrers()))

# Test gc.get_threshold()

print(gc.get_threshold())

# Test
