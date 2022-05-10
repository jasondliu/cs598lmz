import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
print 'After first collect:', gc.garbage
# Test weakref.ref() and weakref.proxy().
print 'Creating references:'
a = {}
a['self'] = a
wr = weakref.ref(a)
p = weakref.proxy(a)
print 'a:', a
print 'wr:', wr
print 'p:', p
print 'p.self is p:', p.self is p
print 'wr() is a:', wr() is a
print 'p.self is wr():', p.self is wr()
print 'Deleting a:'
del a
print 'Collecting:'
gc.collect()
print 'After second collect:', gc.garbage
print 'wr():', wr()
print 'p.self:', p.self
print 'Deleting p:'
del p
print 'Collecting:'
gc.collect()
print 'After third collect:', gc.garbage
print 'wr():', wr()
print 'After clearing:'
gc.garbage = []
print 'Collecting:'
gc.collect
