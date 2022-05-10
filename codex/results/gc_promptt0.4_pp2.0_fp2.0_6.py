import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

w = weakref.ref(f)

gc.collect()

print(gc.collect())
print(gc.garbage)
print(w())

f = None

gc.collect()

print(gc.collect())
print(gc.garbage)
print(w())

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

w = weakref.ref(f)

print(gc.get_referrers(f))
print(gc.get_referrers(f.x))
print(gc.get_referrers(f.x.a))

# Test gc.get_referents()

print(gc.get_referents(f))
print(gc.get_referents(f.x))
print(gc.get_referents(f.x
