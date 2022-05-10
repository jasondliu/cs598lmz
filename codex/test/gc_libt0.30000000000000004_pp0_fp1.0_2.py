import gc, weakref

#------------------------------------------------------------------------------

def _get_weakref_proxy(obj):
    """
    Return a weakref proxy for the given object.
    """
    return weakref.proxy(obj)

#------------------------------------------------------------------------------

def _get_weakref_dict(obj):
    """
    Return a weakref dictionary for the given object.
    """
    return weakref.WeakKeyDictionary()

#------------------------------------------------------------------------------

def _get_weakref_list(obj):
    """
    Return a weakref list for the given object.
    """
    return weakref.WeakKeyDictionary()

#------------------------------------------------------------------------------

def _get_weakref_set(obj):
    """
    Return a weakref set for the given object.
    """
    return weakref.WeakKeyDictionary()

#------------------------------------------------------------------------------

def _get_weakref_weakref(obj):
    """
    Return a weakref weakref for the given object.
    """
    return weakref.ref(obj)

#------------------------------------------------------------------------------

