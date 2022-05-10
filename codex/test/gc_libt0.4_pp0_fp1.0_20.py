import gc, weakref

#
#  Utility functions
#

def _get_weakref(obj, callback=None):
    """
    Return a weak reference to the given object, calling the callback
    if the weak reference dies.
    """
    return weakref.ref(obj, callback)

def _get_weakref_proxy(obj, callback=None):
    """
    Return a weak reference to the given object, calling the callback
    if the weak reference dies. The weak reference is a proxy, so that
    you can perform comparisons and perform hash lookups using the
    weak reference.
    """
    return weakref.proxy(obj, callback)

def _get_weakref_type(obj):
    """
    Return the type of the weak reference to the given object.
    """
    return type(weakref.ref(obj))

