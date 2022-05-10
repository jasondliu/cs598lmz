import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.y = [Foo()]
f.z = [Foo()]

f.y[0].a = f
f.z[0].b = f.x

f_wr = weakref.ref(f)

del f

gc.collect()

print f_wr() is None

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.y = [Foo()]
f.z = [Foo()]

f.y[0].a = f
f.z[0].b = f.x

print gc.get_referrers(f)
print gc.get_referrers(f.x)
print gc.get_referrers(f.y)
print gc.get_referrers(f.z)

# Test gc.get_referents()

class Foo:
    pass

