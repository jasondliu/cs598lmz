import gc, weakref

from . import _GObject
from . import _GObjectBase

def _newGObject(*args, **kwargs):
    """Create a new GObject from the given arguments.
    """
    gobject = _GObject.Object.__new__(_GObject.Object)
    gobject._inst_ptr_ = _GObject._construct(args, kwargs)
    return gobject

def _newGObjectWeakRef(gobject):
    """Create a new weakref for the given GObject.
    """
    if gobject._inst_ptr_ is None:
        raise TypeError("dead object")
    return weakref.ref(gobject, _GObject._weak_ref_cb)

def _newGObjectPtr(ptr, owned=True, type=None):
    """Create a new GObject from a pointer.
    """
    if ptr is None:
        return None
    if type is None:
        type = _GObject.Object
    gobject = _GObject.Object.__new__(type)
    gobject._inst_ptr_ = ptr
