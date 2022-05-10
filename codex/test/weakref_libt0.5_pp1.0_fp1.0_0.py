import weakref

from . import _ffi as ffi
from . import _lib as lib
from . import _util as util


def _get_exception_type(name):
    try:
        return _exception_types[name]
    except KeyError:
        return None

def _make_exception_type(name, base_type, doc=None):
    if name in _exception_types:
        return _exception_types[name]
    new_type = type(name, (base_type,), {'__doc__': doc})
    _exception_types[name] = new_type
    return new_type


class _BaseException(Exception):
    """Base class for all exceptions."""
    pass


class _Error(Exception):
    """Base class for all errors."""
    pass


class _TransientError(_Error):
    """Base class for transient errors."""
    pass


class _FatalError(_Error):
    """Base class for fatal errors."""
    pass


