import weakref
import time
import multiprocessing

class LRUCache(object):
    def __init__(self, size, timeout=60):
        self.size = size
        self.timeout = timeout
        self.cache = OrderedDict()
        self.lock = multiprocessing.Lock()

    def __contains__(self, key):
        try:
            with self.lock:
                item = self.cache[key]
            if time.time() - item[1] > self.timeout:
                with self.lock:
                    del self.cache[key]
                return False
            return True
        except KeyError:
            return False

    def get(self, key):
        with self.lock:
            item = self.cache.pop(key)
            self.cache[key] = item
        if time.time() - item[1] > self.timeout:
            with self.lock:
                del self.cache[key]
            return None
        return item[0]

    def __getitem__(self, key):
        with self.lock
