import weakref

from . import _compat
from . import _exceptions
from . import _utils
from . import _wrappers
from . import _types

__all__ = [
    'Connection',
    'connect',
    'connect_thread',
]

_logger = logging.getLogger(__name__)


class Connection(object):
    """
    A connection to a PostgreSQL server.

    :param str host:
        The host to connect to.

    :param int port:
        The port to connect to on the server.

    :param str database:
        The database to connect to.

    :param str user:
        The user to connect as.

    :param str password:
        The password for the user.

    :param int timeout:
        The timeout for the connection.

    :param bool keepalives:
        Whether to send TCP keepalives.

    :param bool keepalives_idle:
        The number of seconds of inactivity after which a TCP keepalive
        message is sent.

    :param bool keepalives_interval:

