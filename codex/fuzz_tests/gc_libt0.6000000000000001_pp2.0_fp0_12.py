import gc, weakref
from . import _config

class _GCManager(object):
    def __init__(self, gc_threshold=None):
        if gc_threshold is None:
            gc_threshold = _config.get_gc_threshold()
        self._gc_threshold = gc_threshold
        self._objects = []
        self._garbage = []

    def __len__(self):
        return len(self._objects)

    def add(self, obj):
        self._objects.append(weakref.ref(obj))

    def collect(self):
        keep = []
        for obj in self._objects:
            if obj() is not None:
                keep.append(obj)
            else:
                self._garbage.append(obj)
        self._objects = keep
        if len(self._garbage) > self._gc_threshold:
            gc.collect()
            self._garbage = []

_global_gc_manager = _GCManager()

def add_delayed_gc(obj):
    _global_
