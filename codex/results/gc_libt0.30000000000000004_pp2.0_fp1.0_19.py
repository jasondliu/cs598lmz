import gc, weakref

class Class:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Class({!r})'.format(self.name)

def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = Class(name)
        cache[name] = o
        all_refs[name] = o
        del o # decref

    print('  all_refs =', end=' ')
    for name, ref in all_refs.items():
        print('{}={}'.format(name, ref), end=' ')
    print()

    print('\n  Trying to get back one:', end=' ')
    print(cache['one'])
    print('  d[{!r}
