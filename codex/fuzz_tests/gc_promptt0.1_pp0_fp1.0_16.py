import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print "callback called"
    print wr

f = Foo()
wr = weakref.ref(f, callback)
print wr
print wr()
del f
print wr
print wr()
gc.collect()
print wr
print wr()

# Test gc.garbage

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
print wr
print wr()
del f
print wr
print wr()
gc.garbage.append(f)
print wr
print wr()
gc.collect()
print wr
print wr()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
print wr
print wr()
del f
print wr
print wr()
gc.get_referrers(f)
print wr
print wr()
gc.collect()
print wr
print wr()

# Test gc.get_referents()

class Foo:
