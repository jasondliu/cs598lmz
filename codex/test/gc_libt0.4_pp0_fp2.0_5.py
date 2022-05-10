import gc, weakref

def _remove_dead_weakref(wr, wrs):
    'Callback function to remove dead weakrefs from a list.'
    try:
        wrs.remove(wr)
    except ValueError:
        pass

def _remove_dead_weakrefs(wrs):
    'Remove dead weakrefs from a list of weakrefs.'
    for wr in wrs[:]:
        if wr() is None:
            _remove_dead_weakref(wr, wrs)

class WeakMethod(object):
    '''
    Weak reference to a bound method.

    If the referenced method is unbound or deleted, calling the weak reference
    will raise a :exc:`ReferenceError`.

    Weak references to bound methods are used to break reference cycles.
    '''

