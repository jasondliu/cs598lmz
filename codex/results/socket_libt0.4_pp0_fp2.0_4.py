import socket
import sys
import time

from . import const
from . import protocol
from . import util
from . import version

class Client(object):
    """
    An object representing a connection to a server.
    """

    def __init__(self, host, port, timeout=None, reconnect=True,
                 reconnect_delay=3):
        """
        Create a new client connection.

        :param host: The hostname or IP address to connect to.
        :type host: str
        :param port: The port to connect to.
        :type port: int
        :param timeout: The timeout to use for the connection.
        :type timeout: float
        :param reconnect: Whether to attempt to reconnect if the connection
            is lost.
        :type reconnect: bool
        :param reconnect_delay: The number of seconds to wait between
            reconnect attempts.
        :type reconnect_delay: int
        """
        self._host = host
        self._port = port
        self._timeout = timeout
        self._reconnect = reconnect
        self._reconnect_delay = reconnect_delay
       
