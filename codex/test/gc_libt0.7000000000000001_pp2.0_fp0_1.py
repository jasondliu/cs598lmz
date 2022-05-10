import gc, weakref

class MyObject(object):
    def __init__(self):
        print('(Deleting {})'.format(self))

def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    print('CACHE TYPE:', cache_factory)
    ca
