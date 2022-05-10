import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def callback(reference):
    print 'callback(', reference, ')'

f = Foo()
b = Bar()

print 'creating weakrefs'
r1 = weakref.ref(f, callback)
r2 = weakref.ref(b, callback)
print 'created weakrefs'

print 'deleting f'
del f
print 'deleted f'

print 'collecting'
gc.collect()
print 'collected'

print 'deleting b'
del b
print 'deleted b'

print 'collecting'
gc.collect()
print 'collected'

print 'done'
