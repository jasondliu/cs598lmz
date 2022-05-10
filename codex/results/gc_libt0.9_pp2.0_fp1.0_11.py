import gc, weakref

class CachedFunction:
    __version__ = '0.1'
    def __init__ self, f, cache_size=100):
        self.f = f
        self.cache = {}
        self.cache_size = cache_size
        self.__cache_remove_refs = []

    def __call__ self, *args):
        str_args = str(args)
        try:
            return self.__cache_remove_refs[str_args].get()
        except KeyError: pass
        except AttributeError: pass
        # Evict oldest item
        if len(self.__cache_remove_refs) == self.cache_size:
            for r in self.__cache_remove_refs.values(): r.get()
        # Cache new item
        self.cache[str_args] = self.f(*args)
        self.__cache_remove_refs[str_args] = weakref.ref(self.cache[str_args])
        return self.cache[str_args]

    def clear_cache self:
       
