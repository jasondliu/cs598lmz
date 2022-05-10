import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print("callback", wr)

f = Foo()
wr = weakref.ref(f, callback)
print("created", wr)

del f
print("deleted")

gc.collect()
print("collected")

print("done")

# Test gc.garbage

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
print("created", wr)

del f
print("deleted")

gc.garbage.append(wr)
print("appended", wr)

gc.collect()
print("collected")

print("done")

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
print("created", wr)

print("referrers", gc.get_referrers(f))

del f
print("deleted")

gc.collect()
print("collected")

print("done")
