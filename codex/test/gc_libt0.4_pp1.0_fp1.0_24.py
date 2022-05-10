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
