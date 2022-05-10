import weakref
# Test weakref.ref(f)
# Test weakref.proxy(f)
# Test weakref.getweakrefcount(f)
# Test weakref.getweakrefs(f)

def callback(ref):
    print 'callback(', ref, ')'

def test(f):
    print 'creating weak reference'
    r = weakref.ref(f, callback)
    print 'created weak reference', r
    print 'deleting f'
    del f
    print 'f deleted'
    print 'r() is', r()
    print 'calling gc.collect()'
    gc.collect()
    print 'gc.collect() done'
    print 'r() is', r()

def test_proxy(f):
    print 'creating weak proxy'
    p = weakref.proxy(f, callback)
    print 'created weak proxy', p
    print 'deleting f'
    del f
    print 'f deleted'
    print 'p() is', p()
    print 'calling gc.collect()'
    gc.collect()
    print '
