import gc, weakref, sys
from contextlib import contextmanager
from collections import defaultdict

class WeakKeyDictionary:
    def __init__(self):
        self.d = weakref.WeakKeyDictionary()

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        self.d[key] = value

    def __contains__(self, key):
        return key in self.d

    def get(self, key, default=None):
        return self.d.get(key, default)

    def __repr__(self):
        return repr(self.d)

@contextmanager
def debug_gc_cycles(enabled=True):
    """
    Context manager that prints GC cycles to stderr on exit.
    """
    if not enabled:
        yield
        return

    gc_enabled = gc.isenabled()
    gc.disable()

    objs = gc.get_objects()
    refs = defaultdict(list)
    for obj in objs
