import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs
class Foo:
    pass

def callback(reference):
    print 'callback(', reference, ')'
    print '  callback refs:', sys.getrefcount(reference)

def callback2(reference):
    print 'callback2(', reference, ')'
    print '  callback2 refs:', sys.getrefcount(reference)

def test():
    print 'start'
    f = Foo()
    r = weakref.ref(f, callback)
    print 'created weak reference'
    print '  r:', r
    print '  r():', r()
    print '  refcount(r):', sys.getrefcount(r)
    print '  refcount(f):', sys.getrefcount(f)
    print 'del f'
    del f
    print '  r():', r()
    print '  refcount(r):', sys.getrefcount(r)
    print '  gc.collect()'
    gc.collect()
    print '  r():', r()
    print '  ref
