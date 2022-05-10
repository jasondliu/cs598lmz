import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

ref = weakref.ref(f)

del f

gc.collect()

print(ref())

# Test gc.get_objects()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

ref = weakref.ref(f)

del f

gc.collect()

print(ref())

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

ref = weakref.ref(f)

del f

gc.collect()

print(ref())

# Test gc.get_referents()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.a = f

ref = weakref.ref(f)

del f

gc.collect
