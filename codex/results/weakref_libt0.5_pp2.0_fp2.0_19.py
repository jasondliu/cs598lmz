import weakref

from . import _util
from . import _compat
from . import _compat_pickle
from . import _compat_pickle_compat
from . import _compat_pickle_compat_noload
from . import _compat_pickle_compat_noop

from ._util import IS_PYPY, PY2, PY3

from . import _compat_pickle_compat_noop

__all__ = [
    'dumps', 'dump',
    'loads', 'load',
    'HIGHEST_PROTOCOL',
    'DEFAULT_PROTOCOL',
    'Pickler', 'Unpickler',
    'PicklingError', 'UnpicklingError',
    'PickleBuffer', 'PickleBytes',
    'PickleString', 'PickleStream',
    'HANDLE_ERRORS', 'HANDLE_EOF', 'HANDLE_SHORT', 'HANDLE_LONG',
    'HANDLE_INT', 'HANDLE_BININT', 'H
