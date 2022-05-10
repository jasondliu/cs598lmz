import socket
import sys
import threading
import time

from . import constants
from . import messages
from . import utils
from . import exceptions

class Client(object):
    """
    A client for the MQTT protocol.

    This class implements the client side of the MQTT protocol. It can be used
    to connect to a broker and publish messages to the broker.

    :param host: Hostname or IP address of the broker to connect to.
    :type host: str
    :param port: Port number of the broker to connect to.
    :type port: int
    :param keepalive: Maximum period in seconds allowed between communications
                      with the broker. If no other messages are being exchanged
                      the client sends a PINGREQ message to the broker.
    :type keepalive: int
    :param clean_session: If set to 0, the broker will store the subscription
                          and pending messages when the client disconnects.
                          When the client reconnects, it receives the stored
                          messages. If set to 1, the client and broker discard
                          any previous session and start a new one
