import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

print gc.collect()
print gc.collect()
print gc.collect()

del f

print gc.collect()
print gc.collect()
print gc.collect()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

print gc.get_referrers(f)
print gc.get_referrers(f.x)
print gc.get_referrers(f.x.a)

del f

print gc.get_referrers(f)
print gc.get_referrers(f.x)
print gc.get_referrers(f.x.a)

# Test gc.get_referents()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.
