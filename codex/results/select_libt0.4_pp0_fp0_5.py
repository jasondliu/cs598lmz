import select
import socket
import sys
import threading
import time

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import messages
from . import protocol

from .utils import logger
from .utils import log_level


class Client(object):
    """
    Implements the client side of the MQTT v3.1.1 protocol.

    This is the main class for Paho MQTT Python client library, and
    implements the MQTT v3.1.1 protocol.

    It provides an interface for communicating with an MQTT server.

    """

    def __init__(self, client_id="", clean_session=True, userdata=None,
                 protocol=constants.MQTTv311, transport="tcp"):
        """
        Create a new client instance.

        :param client_id: The unique client id string used when connecting to
                          the broker. If client_id is zero length or None,
                          then one will be randomly generated.
        :param clean_session: If True, the broker will
