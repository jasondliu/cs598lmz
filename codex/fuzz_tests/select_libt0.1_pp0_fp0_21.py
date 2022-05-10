import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import messages
from . import protocol
from . import util

_logger = log.get_logger(__name__)


class _Connection(object):
    """
    A connection to a remote peer.

    This class is not thread-safe.
    """

    def __init__(self, peer_id, socket, address, is_inbound):
        self._peer_id = peer_id
        self._socket = socket
        self._address = address
        self._is_inbound = is_inbound
        self._is_connected = False
        self._is_disconnected = False
        self._is_disconnecting = False
        self._is_closing = False
        self._is_closed = False
        self._is_reading = False
        self._is_writing = False
        self._is_writing_message = False
        self._is_writing_message
