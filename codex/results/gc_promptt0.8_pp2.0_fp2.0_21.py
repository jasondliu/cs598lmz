import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class Foo(object):
    pass
f = Foo()
def ref():
    print 'called'
wr = weakref.ref(f, ref)
gc.collectable(wr)
del f
gc.collectable(wr)
gc.collectable(weakref.ref(1))
