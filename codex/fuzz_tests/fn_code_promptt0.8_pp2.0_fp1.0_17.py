fn = lambda: None
# Test fn.__code__ to check Python version
fn.__code__ = True

if fn.__code__:
    # Python 2.x
    int = long
    basestring = basestring
    unicode = unicode
    import cPickle as pickle
    cmp = cmp
    class_types = (type, types.ClassType)
    Iterator = Iterator
    callable = callable
    from itertools import ifilter

else:
    # Python 3.x
    int = int
    basestring = (str,)
    unicode = str
    import pickle
    cmp = lambda a, b: (a > b) - (a < b)
    class_types = (type,)
    Iterator = object
    callable = lambda obj: getattr(obj, '__call__', False)
    ifilter = filter


del fn


#===============================================================================
# Iterable
#===============================================================================

def iterable(obj):
    if isinstance(obj, Iterator):
        return False
    try:
        iter(obj)

