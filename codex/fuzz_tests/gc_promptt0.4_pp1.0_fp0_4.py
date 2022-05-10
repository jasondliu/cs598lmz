import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()

def callback(wr):
    print "callback called"

wr = weakref.ref(f, callback)

print wr()

del f
print wr()

gc.collect()
print wr()

gc.collect()
print wr()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()

def callback(wr):
    print "callback called"

wr = weakref.ref(f, callback)

print wr()

del f
print wr()

gc.collect()
print wr()

gc.collect()
print wr()

# Test gc.get_referents()

class Foo:
    pass

f = Foo()

def callback(wr):
    print "callback called"

wr = weakref.ref(f, callback)

print wr()

del f
print wr()

gc.collect()
print wr()

gc.collect()
print wr()

# Test gc
