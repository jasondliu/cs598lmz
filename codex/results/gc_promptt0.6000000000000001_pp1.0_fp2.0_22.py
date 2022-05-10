import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
class Test:
    pass

def callback(obj):
    print 'deleted', obj

o = Test()
r1 = weakref.ref(o, callback)
r2 = weakref.ref(o, callback)

print r1, r2
print r1() is o
print r2() is o

print 'deleting o'
del o
print 'collecting'
gc.collect()
print 'done'

# Test gc.collect() with weakrefs, when the callback itself has a reference
# to the object.
class Test:
    pass

def callback(obj):
    print 'deleted', obj
    print 'callback has ref to', r2()

o = Test()
r1 = weakref.ref(o)
r2 = weakref.ref(o, callback)

print r1, r2
print r1() is o
print r2() is o

print 'deleting o'
del o
print 'collecting'
gc.collect()
print 'done'

# Test g
