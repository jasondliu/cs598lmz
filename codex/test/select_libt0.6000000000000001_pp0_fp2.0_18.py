import select
import socket
import sys
import threading
import time

from . import constants, logging
from .packet import Packet, PacketType
from .utils import get_tcp_socket, get_udp_socket

log = logging.getLogger(__name__)


class Sender:
    """
    A Sender object is used to send a file to a Receiver object over a socket.
    """

    def __init__(self, host, port, filename, udp_port=None, udp_timeout=None):
        """
        Initialize a Sender object.

        :param host: The hostname to connect to
        :type host: str
        :param port: The port to connect to
        :type port: int
        :param filename: The name of the file to send
        :type filename: str
        :param udp_port: The port to use for UDP connections
        :type udp_port: int
        :param udp_timeout: The timeout for UDP connections
        :type udp_timeout: int
        """
        self.host = host
