import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print "called back"

f = Foo()
wr = weakref.ref(f, callback)
print wr() is f
print gc.collect()
print wr() is f
f = None
print gc.collect()
print wr()

# Test gc.get_objects()

class Foo:
    pass

f = Foo()

objs = gc.get_objects()
print len([o for o in objs if isinstance(o, Foo)])
print len([o for o in objs if isinstance(o, dict)])

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()

objs = gc.get_referrers(f)
print len([o for o in objs if isinstance(o, dict)])
print len([o for o in objs if isinstance(o, list)])

# Test gc.get_referents()

class Foo:
    pass

f
