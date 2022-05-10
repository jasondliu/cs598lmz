import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

foo = Foo()

def callback(wr):
    print "called back with", wr

wr = weakref.ref(foo, callback)

print "created ref", wr
print "foo is", foo
print "foo refcount is", sys.getrefcount(foo)

print "calling gc.collect()"
gc.collect()

print "foo is", foo
print "foo refcount is", sys.getrefcount(foo)

print "deleting foo"
del foo

print "foo is", foo
print "foo refcount is", sys.getrefcount(foo)

print "calling gc.collect()"
gc.collect()

print "foo is", foo
print "foo refcount is", sys.getrefcount(foo)
