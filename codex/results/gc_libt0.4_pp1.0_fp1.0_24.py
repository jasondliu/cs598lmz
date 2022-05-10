import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

def demo(cache_factory):
    # populate the cache with some objects
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = MyClass(name)
        cache[name] = o
    print 'After population:', cache.keys()

    # remove some of the objects
    del o
    del cache['one']
    print 'After removing one:', cache.keys()

    # take a list of the values
    l = cache.values()
    print 'Values:', l

    # clear the cache
    cache.clear()
    print 'After clearing:', cache.keys()

    # show that the list is now empty
    print 'Values:', l

print 'Without weak values:'
demo(dict)

print
print 'With weak values:'
demo(weakref.WeakValueD
