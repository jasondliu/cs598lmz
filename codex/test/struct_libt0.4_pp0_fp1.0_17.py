import _struct

from . import _compat
from . import _util
from . import _errors
from . import _types
from . import _constants
from . import _message
from . import _c_api

__all__ = ['Connection']

_connection_class_lock = _compat.threading.Lock()
_connection_class_registry = {}


def register_connection(protocol_version, connection_class):
    with _connection_class_lock:
        _connection_class_registry[protocol_version] = connection_class


def get_connection_class(protocol_version):
    with _connection_class_lock:
        return _connection_class_registry.get(protocol_version, Connection)


class Connection(object):
    """
    A connection to a Cassandra cluster.
    """

