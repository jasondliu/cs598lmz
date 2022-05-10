import gc, weakref

#------------------------------------------------------------------------------
#
#  Some utility functions for working with weakrefs.
#
#------------------------------------------------------------------------------

def weak_ref (obj):
    """
    Return a weak reference to the given object.  If the object is already a
    weak reference, return it.
    """
    if isinstance (obj, weakref.ref):
        return obj
    return weakref.ref (obj)

def weak_proxy (obj):
    """
    Return a weak proxy to the given object.  If the object is already a weak
    proxy, return it.
    """
    if isinstance (obj, weakref.ProxyType):
        return obj
    return weakref.proxy (obj)

def weak_ref_get (obj):
    """
    Return the object referenced by the given weak reference or weak proxy.
    """
    if isinstance (obj, weakref.ref):
        return obj ()
    if isinstance (obj, weakref.ProxyType):
        return obj
    return obj

