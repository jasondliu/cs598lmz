import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print 'in bar'

f = Foo()
f.x = bar
f.x()

print 'before weakref'
wr = weakref.ref(f)
print 'after weakref'

print 'before del f'
del f
print 'after del f'

print 'before gc.collect()'
gc.collect()
print 'after gc.collect()'

print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print 'wr() is', wr()
print '
