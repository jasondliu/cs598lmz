import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
a.append(a)
b = []
b.append(b)
b = None
# Get some statistics
print 'Collecting...'
n = gc.collect()
print 'Unreachable objects:', n
print 'Remaining Garbage:', gc.garbage

# Test weak references
class C(object):
    pass

s = C()
r = weakref.ref(s)
print 'Object referred to by weak reference:', r()
del s
print 'Collecting...'
n = gc.collect()
print 'Unreachable objects:', n
print 'Object referred to by weak reference:', r()

# Test cyclic garbage detection
class C(object):
    pass

a = C()
a.b = C()
a.b.a = a
del a
print 'Collecting...'
n = gc.collect()
print 'Unreachable objects:', n
print 'Remaining Garbage:', gc.garbage

# Test gc.get_referrers() and gc.get_
