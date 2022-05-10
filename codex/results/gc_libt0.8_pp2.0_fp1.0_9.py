import gc, weakref
import sys, traceback
import itertools, exceptions

_cache = {}

def reduce(obj, protocol=None, *, level=None):
    """Return a string containing a byte-stream representation
    of obj.  obj must be a type that the pickle module can handle.
    protocol defaults to the highest protocol supported by pickle.

    If keyword args are present, they will be pickled as well and a
    pickled representation of their values will be prepended to the
    returned string, so that when the string is unpickled the same
    objects are supplied to the unpickling functions.
    """

    proto = umsgpack.default.PROTOCOL if protocol is None else protocol
    return dumps(obj, protocol=proto, level=level)


def dumps(obj, protocol=None, *, level=None):
    """Return the pickled representation of the object as a bytes object.

    The optional *protocol* argument tells the pickler to use the given
    protocol; supported protocols are 0, 1, 2, 3 and 4.  The default
    protocol is 3; a
