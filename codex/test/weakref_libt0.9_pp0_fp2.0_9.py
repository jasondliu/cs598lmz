import weakref
import six

from cassandra import DriverException
from cassandra.util import unique_id_from_uuid1
from cassandra.protocol import ServerErrorMessage
from cassandra.pool import Host
from cassandra.pool import HostConnection
from cassandra.protocol import RegisterMessage
from cassandra.protocol import EventMessage

from cassandra.query import SimpleStatement, StatementException

try:
    import unittest2 as unittest
    from mock import MagicMock, Mock, patch
except ImportError:
    import unittest
    from unittest.mock import MagicMock, Mock, patch


UUID1 = unique_id_from_uuid1(0, 0)
UUID3 = unique_id_from_uuid1(2, 0)


def cmp(a, b):
    return (a > b) - (a < b)


