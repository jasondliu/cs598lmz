import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class Foo:
    pass

def callback(r):
    print 'callback called'
    print 'r():', r()

f = Foo()

r = weakref.ref(f, callback)
print 'created weak reference r:', r

print 'deleting f'
del f

print 'collecting'
gc.collect()

print 'done'

# Test gc.collect with cycles

class Foo:
    pass

f1 = Foo()
f2 = Foo()
f1.f = f2
f2.f = f1

print 'created cycle'

print 'collecting'
gc.collect()

print 'done'

# Test gc.collect with finalizers

class Foo:
    pass

def callback(r):
    print 'callback called'
    print 'r():', r()

f = Foo()

r = weakref.ref(f, callback)
print 'created weak reference r:', r

f.r = r

del f

print 'collecting'
