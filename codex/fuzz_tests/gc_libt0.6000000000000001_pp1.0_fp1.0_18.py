import gc, weakref

def _make_key(args, kwds, typed,
             kwd_mark = (object(),),
             fasttypes = set((int, str, frozenset, type(None))),
             sorted=sorted, tuple=tuple, type=type, len=len):
    """Make a cache key from optionally typed positional and keyword arguments"""
    key = args
    if kwds:
        sorted_items = sorted(kwds.items())
        key += kwd_mark
        for item in sorted_items:
            key += item
    if typed:
        key += tuple(type(v) for v in args)
        if kwds:
            key += tuple(type(v) for k, v in sorted_items)
    elif len(key) == 1 and type(key[0]) in fasttypes:
        return key[0]
    return tuple(key)

def lru_cache(maxsize=100, typed=False):
    """Least-recently-used cache decorator.

    Arguments to the cached function must be hashable.

