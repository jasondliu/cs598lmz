import weakref

from . import _ffi
from . import _lib
from . import _util
from . import _errors
from . import _types
from . import _version

__all__ = ['Session', 'SessionOptions', 'SessionStats']


class SessionOptions(object):
    """
    Options for a WiredTiger session.

    The values are configured by the application, and are used by
    :meth:`wiredtiger.Connection.open_session` to configure a
    :class:`wiredtiger.Session`.

    :param str isolation: the default isolation level for transactions
      started through the session.  The default isolation level is
      :attr:`~wiredtiger.constants.isolation_level.READ_COMMITTED`.

    :param str name: the name of the session, used for debugging
      purposes.

    :param str transaction_sync: the method used to ensure transaction
      durability.  The default setting is ``"dsync"``.  See
      :attr:`~wiredtiger.constants.transaction_sync` for possible
      values.

    :
