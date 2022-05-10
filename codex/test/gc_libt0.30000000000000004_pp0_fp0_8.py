import gc, weakref

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass({!r})'.format(self.name)

gc.set_debug(gc.DEBUG_SAVEALL)

def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = MyClass(name)
        cache[name] = o
        all_refs[name] = o
        del o # remove the reference

    print('  all_refs =', end=' ')
    print(all_refs)
    print('\nBefore, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print(' {} = {}'.format(name, value))
       
