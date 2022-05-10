import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
class C:
    pass

def callback(wr, gc_was_enabled):
    print 'called back', wr, gc_was_enabled
    if gc_was_enabled:
        gc.enable()

c = C()
wr = weakref.ref(c, callback)
print 'created', wr

gc.collect()
print 'collected'

print 'disabling'
gc.disable()
print 'enabled?', gc.isenabled()

print 'deleting c'
del c

print 'enabled?', gc.isenabled()
print 'collecting'
gc.collect()
print 'collected'

print 're-enabling'
gc.enable()
print 'enabled?', gc.isenabled()

print 'creating c'
c = C()
print 'created c'
print 'collecting'
gc.collect()
print 'collected'

print 'deleting c'
del c
print 'collecting'
gc.collect()
print 'collected'
