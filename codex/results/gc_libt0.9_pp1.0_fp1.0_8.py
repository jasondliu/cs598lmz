import gc, weakref, sys, marshal, types, inspect, warnings

_original_uniqueid_function = id
_unique_ids = weakref.WeakKeyDictionary()

# this function is designed to have the same quirks as CPython - every
# object has exactly one id
def uniqueid(x):
    t = type(x)
    if t is str:
        return _uniqueid_for_string(x)
    try:
        return _unique_ids[x]
    except (KeyError, TypeError): # TypeError is for built-in types
        try:
            _unique_ids[x] = _original_uniqueid_function(x)
        except TypeError:
            # try to weakref the object, get a unique id from it, and
            # possibly add it to the dict
            y = weakref.ref(x)
            _unique_ids[y] = _original_uniqueid_function(y)
            return uniqueid(y)
    return _unique_ids[x]

# hashing of short strings is completely different in CPython, we
# implement the same algorithm
