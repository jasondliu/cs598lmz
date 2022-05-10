import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

def demo(cache_factory):
    # populate the cache with some objects
    cache = cache_factory()
    objs = [MyClass(repr(i)) for i in range(3)]
    for o in objs:
        cache[o] = o
    print '  in cache:', cache.keys()
    del objs # remove the list from the current namespace

    # run a garbage collection right away
    print '\nBefore, number of objects:', len(gc.get_objects())
    gc.collect()
    print 'After, number of objects:', len(gc.get_objects())

    # show that the objects were collected
    print '\n  in cache:', cache.keys()

print 'Without weak references:'
demo(dict)

print '\nWith weak references:'
demo(weakref.WeakValueD
