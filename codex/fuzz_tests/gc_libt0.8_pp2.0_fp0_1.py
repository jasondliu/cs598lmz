import gc, weakref, sys
from types import ClassType
from UserDict import UserDict, UserList, UserString


# Various helpers for testing and debugging:

def test(**kwargs):
    """Run doctests, unittests, whatever."""
    import doctest
    from py.test import cmdline
    sys.exit(cmdline.main(**kwargs))

def get_size(obj, seen=None):
    """Recursively iterate to sum size of object & members."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    objid = id(obj)
    if objid in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(objid)
    if hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    if isinstance(obj, dict):
        size += sum((get_size(v, seen) for v in obj.values
