import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

class B:
    pass

def callback(wr):
    print 'callback'
    print wr
    print wr()
    print

a = A()
b = B()

wr = weakref.ref(a, callback)
print 'created wr'
print wr
print wr()
print

print 'deleting a'
del a
print 'calling gc.collect'
gc.collect()
print 'done'
print

print 'creating a'
a = A()
print 'created a'
print

print 'creating wr'
wr = weakref.ref(a, callback)
print 'created wr'
print wr
print wr()
print

print 'deleting a'
del a
print 'calling gc.collect'
gc.collect()
print 'done'
print

print 'creating a'
a = A()
print 'created a'
print

print 'creating wr'
wr = weakref.ref(a)
print 'created wr'
print wr
