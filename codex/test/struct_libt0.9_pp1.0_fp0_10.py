import _struct
import _libmspack
import _libmspack_low

dump = os.environ.get( "DUMP", False )

def wrap_simple(fn):
    """
    A decorator for the simple wrapper functions.
    """
    def _inner(cls, *args):
        return fn(cls.handle, *args)
    _inner.__name__ = fn.__name__
    _inner.__doc__ = fn.__doc__
    return _inner

def wrap_complicated(fn):
    """
    A decorator for the more complicated wrapper functions.
    """
    def _inner(cls, *args):
        args = list(args)
        args[0] = cls.handle
        return fn(*args)
    _inner.__name__ = fn.__name__
    _inner.__doc__ = fn.__doc__
    return _inner

