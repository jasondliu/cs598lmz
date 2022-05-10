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
