import gc, weakref

def show_refs(obj):
    print 'Object refs:', [r for r in gc.get_referents(obj)
                           if isinstance(r, weakref.ReferenceType)]

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self

def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    print 'CACHE TYPE:', cache_factory
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject()
        cache[name] = o
        all_refs[name] = o
        del o # decref

    print '  all_refs =',
    show_refs(all_refs)
    print '\nBefore, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s
