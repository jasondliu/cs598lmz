import gc, weakref
import gc, weakref
from weakref import WeakKeyDictionary

def get_cache_stats():
    return (
        len(weakref.getweakrefs(obj)),
        len([o for o in gc.get_objects() if isinstance(o, weakref.ProxyType)]),
        len([o for o in gc.get_objects() if isinstance(o, weakref.CallableProxyType)]),
        )

# A function that caches its arguments.  Modified from
# http://code.activestate.com/recipes/325205-cache-decorator-in-decorator-python/
class cached(object):
    def __init__(self, func):
        self.func = func
        self.cache = WeakKeyDictionary()

    def __call__(self, *args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in self.cache:
            return self.cache[key]
        else:
            result = self.func(*args, **kwargs)
            self
