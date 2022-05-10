import weakref

import gc

###############################################################################################
# utils
###############################################################################################

# objects to keep references to
objects = set()

# sorted list of object types to keep
keep_types = [weakref.ReferenceType, weakref.CallableProxyType, weakref.ProxyType]

# a list of dicts of weak references to the objects
weak_objects = {}

def _is_weak(obj):
    otype = type(obj)
    if otype not in keep_types:
        return True
    return False

def _weak_ref(obj):
    """
        returns a weak reference to the object
    """
    return weakref.ref(obj)

def _get_objects():
    """
        get all objects in memory
    """
    for i in gc.get_objects():
        yield i

def _get_weak_refs():
    for i in gc.get_objects():
        if _is_weak(i):
            yield i

