import weakref

from collections import defaultdict

class _WeakValueDictionary(weakref.WeakValueDictionary):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = threading.Lock()
    
    def __setitem__(self, key, value):
        with self._lock:
            super().__setitem__(key, value)
    
    def __getitem__(self, key):
        with self._lock:
            return super().__getitem__(key)
    
    def __delitem__(self, key):
        with self._lock:
            super().__delitem__(key)
    
    def __len__(self):
        with self._lock:
            return super().__len__()
    
    def get(self, key, default=None):
        with self._lock:
            return super().get(key, default)

