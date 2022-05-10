import types
types.FunctionType.__repr__ = lambda self: "<function %s at 0x%x>" % (self.__name__, id(self))

#=============================================================================
# Misc
#=============================================================================

def get_class_name(obj):
    return obj.__class__.__name__

#=============================================================================
# Profiling
#=============================================================================

class Profiler(object):

    def __init__(self):
        self._stats = defaultdict(list)

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._end = time.time()

    def add_stat(self, name, value):
        self._stats[name].append(value)

    def get_stat(self, name):
        return self._stats[name]

    def get_stats(self):
        return dict(self._stats)

    def get_elapsed(self):
        return self._end - self._start

    def __str__
