import weakref

from . import _util
from . import _compat
from . import _error
from . import _query
from . import _result
from . import _transaction
from . import _types
from . import _helpers


def _trace_callback(handle, name, sql, callback):
    """Called by SQLite when a trace event occurs."""
    callback(TraceEvent(name, sql))


def _profile_callback(handle, name, sql, callback):
    """Called by SQLite when a profile event occurs."""
    callback(ProfileEvent(name, sql))


def _authorize_callback(handle, action, arg1, arg2, dbname, callback):
    """Called by SQLite when an authorization event occurs."""
    return callback(AuthorizationEvent(action, arg1, arg2, dbname))


class Connection(object):
    """
    A SQLite database connection object.
    """

    def __init__(self, database, timeout=5.0, detect_types=0, isolation_level=None,
                 check_same_thread=
