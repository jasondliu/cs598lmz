import weakref

def make_weakref_key(obj):
    """Return a key that can be used in a dictionary to weakly reference an
    object"""
    return weakref.ref(obj)

class Unpicklable(Exception):
    pass

def make_weakref_key_unpicklable(obj):
    """Convert a picklable key (as returned by make_weakref_key) into an
    unpicklable one that can be used in a weakref.WeakKeyDictionary"""
    if not isinstance(obj, weakref.ref):
        raise ValueError("Obj must be a weakref")
    return obj

def dict_subset(d, ks):
    """Return a new dictionary that is a subset of the given dictionary
    containing only the keys in the provided list"""
    assert isinstance(ks, set)
    return dict((k, v) for k, v in d.items() if k in ks)

def dict_union(*ds):
    """Return a new dictionary that is the union of all provided dictionaries"""
    r = {}
   
