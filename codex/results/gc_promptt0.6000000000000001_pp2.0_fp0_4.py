import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after weakrefs are created.
gc.collect()

class A:
    pass

a = A()
w = weakref.ref(a)
del a
gc.collect()
print 'Before del:', gc.get_referrers(w)
del w
gc.collect()
print 'After del:', gc.get_referrers(w)

# Test gc.collect() before and after weakrefs are created.
gc.collect()

class A:
    pass

a = A()
w = weakref.ref(a)
gc.collect()
print 'Before del:', gc.get_referrers(w)
del a
del w
gc.collect()
print 'After del:', gc.get_referrers(w)

# Test gc.collect() before and after weakrefs are created.
gc.collect()

class A:
    pass

a = A()
w = weakref.ref(a)
del a
gc.collect()
print 'Before del:', gc.
