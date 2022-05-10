import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect Here
import gc, weakref
# Test gc.garbage
import gc, weakref
class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))
def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject()
        cache[name] = o
        all_refs[name] = o
        del o # decref
    
    print('all_refs =', end=' ')
    for name, value in all_refs.items():
        print('{} = {!r}'.format(name, value), end=' ')
    print()
    
    print('cache before, count = ', len(cache))
    for name, value in cache.items():
        print('{} = {!r}'.format(name, value), end
