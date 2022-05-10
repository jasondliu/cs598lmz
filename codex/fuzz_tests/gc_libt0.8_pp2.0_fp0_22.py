import gc, weakref
import threading, functools

# in python3, list.index is O(n), which is horrible for
# list-with-indexes, so we use our own indexer
class indexer(collections.MutableMapping, ThreadSafeMixin):
    def __init__(self, build_index=False, *a, **kw):
        self.__dict__['_items'] = {}
        self.__dict__['_idx'] = []
        self.__dict__['_vers'] = 0
        ThreadSafeMixin.__init__(self, *a, **kw)
        if build_index:
            self._idx = list(self._items.keys())
            self._vers = self._newvers()

    def __len__(self):
        self._lock_acquire()
        try:
            return len(self._idx)
        finally:
            self._lock_release()

    def _newvers(self):
        return self._vers + 1

    def mutate(self, func, *args, **kwargs):
        """
