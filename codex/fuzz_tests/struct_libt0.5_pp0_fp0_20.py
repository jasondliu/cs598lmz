import _struct

from . import utils
from . import errors
from . import constants
from . import types


class Encoder(object):
    """
    Encoder is used to encode Python objects into a Cassandra-specific
    binary protocol.

    This class shouldn't be used directly, use L{Cluster.connect()} to obtain a
    Session object.

    Example usage::

        >>> session = cluster.connect("mykeyspace")
        >>> session.execute("CREATE TABLE mytable (k int PRIMARY KEY, v int)")

        >>> session.execute("INSERT INTO mytable (k, v) VALUES (%s, %s)",
        ...                 (0, 0))
        <cassandra.cluster.ResultSet object at 0x7fa9b9f9b790>

        >>> prepared = session.prepare("INSERT INTO mytable (k, v) VALUES (?, ?)")

        >>> session.execute(prepared, (1, 1))
        <cassandra.cluster.ResultSet object at 0x7fa9b9f9bb10>

        >>> session.execute("
