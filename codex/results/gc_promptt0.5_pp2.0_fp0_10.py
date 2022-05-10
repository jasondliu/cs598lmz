import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo:
    pass

def callback(wr):
    print 'callback', wr

def test_callback(n):
    print 'test_callback', n
    for i in range(n):
        foo = Foo()
        wr = weakref.ref(foo, callback)
        wr()
        foo = None
    gc.collect()
    print 'done test_callback', n

test_callback(2)
test_callback(3)
test_callback(4)
print 'done'
 
gc.set_debug(0)
