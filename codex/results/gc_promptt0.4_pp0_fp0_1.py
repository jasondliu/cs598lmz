import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def callback(x):
    print "callback", x

f = Foo()
c = weakref.ref(f, callback)
print c
print c()
print f
del f
print gc.collect()
print c()

# Test gc.get_referrers()

class Foo(object):
    pass

f = Foo()
r = gc.get_referrers(f)
print r

# Test gc.get_referents()

class Foo(object):
    pass

f = Foo()
r = gc.get_referents(f)
print r

# Test gc.get_objects()

class Foo(object):
    pass

f = Foo()
r = gc.get_objects()
print r

# Test gc.is_tracked()

class Foo(object):
    pass

f = Foo()
print gc.is_tracked(f)

# Test gc.garbage

class Foo(object):
