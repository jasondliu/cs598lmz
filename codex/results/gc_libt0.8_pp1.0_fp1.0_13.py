import gc, weakref, abc
from numpy import zeros, ndarray

from .refcount import refcount, refs

__all__ = [
    'wrap_in_refs', 'unwrap_ref', 'make_shared_array', 'share_data',
    'SharedArray', 'SharedArrayView', 'SharedNdarray', 'SharedNdarrayView',
    'SharedArrayABC', 'SharedNdarrayABC', 'SharedNdarrayMeta',
    'SharedArrayBase', 'SharedArrayBaseMeta'
]

_UNDEFINED = object()

def wrap_in_refs(obj):
    '''
    Wrap a object in a weakref that is stored in a list.

    Parameters
    ----------
    obj : object
        The object to be wrapped.

    Returns
    -------
    ref : weakref
        The weakref to the object.
    '''
    tmp = [weakref.ref(obj)]
    return refcount(tmp[0])

def unwrap_ref(ref):
    '''
   
