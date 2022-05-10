import select
import sys
import time

from . import log
from . import utils
from .protocol import Protocol
from . import protocol
from . import constants

class Client(object):
    """
    A client for the ZeroMQ messaging system.

    :param context: The context to use for the client.
    :type context: :class:`zmq.core.context.Context`
    :param str endpoint: The endpoint to connect to.
    :param str identity: The identity to use for the client.
    :param int timeout: The timeout to use for the client.
    :param bool reconnect: Whether or not the client should reconnect.
    :param int reconnect_interval: The interval to use when reconnecting.
    :param int heartbeat_interval: The interval to use for heartbeats.
    :param int heartbeat_timeout: The timeout to use for heartbeats.
    :param bool verbose: Whether or not to use verbose logging.
    """

    def __init__(self, context, endpoint, identity=None, timeout=None,
                 reconnect=True, reconnect_interval=
