import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo(object):
    def __del__(self):
        print "Deleting Foo"

def bar():
    foo = Foo()
    foo.x = Foo()
    return foo

f = bar()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "Collecting"
gc.collect()
print "
