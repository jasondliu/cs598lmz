import gc, weakref
from collections import defaultdict
from itertools import chain

from functools import wraps


def memoize(f):
    cache = {}

    @wraps(f)
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapper


def weak_memoize(f):
    cache = weakref.WeakValueDictionary()

    @wraps(f)
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapper


def clear_memoize_cache(f):
    f.cache.clear()


class Memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__
