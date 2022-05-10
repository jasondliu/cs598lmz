import select
import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import messages
from . import utils

__all__ = ['Client']


class Client(object):
    """
    A client for the MQTT v3.1.1 protocol.

    This class implements threaded interfaces to the network layer,
    so that the client can publish and subscribe while waiting for
    data asynchronously.

    :param str client_id: The client ID for this client. If `None`, a random
        client ID will be generated. If `0`, a client ID will not be used.
    :param bool clean_session: If `True`, the broker will remove all
        information about this client when it disconnects. If `False`, the
        client is a durable client and subscription information and queued
        messages will be retained when the client disconnects. Defaults to
        `True`.
    :param str userdata: User data that is passed to callbacks.
    :param int protocol: The MQTT version to use for this client.
        Defaults to `3`
