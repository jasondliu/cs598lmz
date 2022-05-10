import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before creating a weakref
gc.collect()

# Check id() of weakly referencable objects
a = {}; b = {}; c = {}
# Test weakref constructor
r1 = weakref.ref(a)
print 'r1:', r1
print 'r1():', r1()
print 'hash(r1):', hash(r1)
# Test getweakrefcount()
print 'getweakrefcount():', weakref.getweakrefcount(a)
# Test getweakrefs()
print 'getweakrefs():', weakref.getweakrefs(a)
r2 = weakref.ref(b)
r3 = weakref.ref(c)
r4 = weakref.ref(a)
print 'getweakrefs():', weakref.getweakrefs(a)

# Test callbacks
def callback(object): print "called back"
w1 = weakref.ref(a, callback)
w2 = weakref.ref(b, callback)

# Test callbacks with extra arguments
def callback2(object, arg1, arg
