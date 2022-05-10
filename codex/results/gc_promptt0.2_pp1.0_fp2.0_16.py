import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print 'callback called'
    print wr()

f = Foo()
wr = weakref.ref(f, callback)

print 'before del f'
print wr()
del f
print 'after del f'
print wr()

print 'before gc.collect()'
gc.collect()
print 'after gc.collect()'
print wr()

print 'before gc.collect()'
gc.collect()
print 'after gc.collect()'
print wr()
