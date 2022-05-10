import weakref
import threading
import multiprocessing

#
# Helper functions
#
def get_id(obj):
    """Return an unique identifier for the object."""
    if not isinstance(obj, _dlopen._CTypePtrOrArray):
        return id(obj)
    if obj:
        addr = obj.value
    else:
        addr = 0
    return addr

def get_refs(obj):
    """
    Return the list of objects which refer to the object.
    """
    if isinstance(obj, _dlopen._CTypePtrOrArray):
        return _get_refs(obj)
    else:
        return obj.__weakref__

def _get_refs(obj):
    """
    Return the list of objects which refer to the object.
    """
    refs = []
    if obj:
        addr = obj.value
    else:
        addr = 0
    for ref in gc.get_referrers(obj):
        if isinstance(ref, _dlopen._CTypePtrOrArray):
           
