import gc, weakref, os, pstats, time, cProfile
from log import log

def number_of_live_objects(cls):
    """
    Return the number of live objects of type `cls`.
    """
    cls_ref = weakref.ref(cls)
    def is_cls(wr):
        obj = wr()
        return obj and obj.__class__ is cls_ref()
    return len(filter(is_cls, gc.get_referrers(cls)))

def total_memory_usage():
    """
    Return the total memory usage reported by the garbage collector.
    """
    return gc.get_count()[0]

def mem_profile(code, globals=None, locals=None, enabled=log.level >= log.profile,
    plot=True, plot_limit=200, profile=True, gc_collect=False):
    """
    Evaluate `code` in the given namespace and plot a graph of the memory
    usage.
    """
    if not enabled: return None
    # Get the namespaces
