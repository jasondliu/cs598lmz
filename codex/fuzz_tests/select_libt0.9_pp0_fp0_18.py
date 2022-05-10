import select
import signal
import traceback
import threading

from pyshka import logger
from pyshka.util import config


class BaseConfig(object):
    """Config object for :class:`pyshka.client.BaseClient`.

    """
    _reserve = None

    _config = None
    """Client config
    :type: :class:`pyshka.util.config.Config`

    """
    _expires = None
    _handlers = None
    _io_loop = None
    _io_loop_thread = None
    _raw_io_loop_thread = None
    _recv_handler = None
    _send_handler = None
    _stopped = None
    """Used to signal when client has stopped
    :type: :class:`threading.Event`

    """


class BaseClient(BaseConfig):
    """Represents a PyShka Client.

    This is a base class that should not be instantiated.
    It provides the base methods which can be overridden by
    implementing classes.

    """
    _
