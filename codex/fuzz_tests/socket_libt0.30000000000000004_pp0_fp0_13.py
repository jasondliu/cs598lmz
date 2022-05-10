import socket
import sys
import threading
import time
import traceback

from . import util
from . import constants
from . import exceptions
from . import packet
from . import protocol

logger = logging.getLogger(__name__)

class Client(object):
    """
    A client for the Minecraft Pi protocol.
    """

    def __init__(self, host='localhost', port=constants.DEFAULT_PORT):
        """
        Create a new client.

        :param host: The host to connect to.
        :param port: The port to connect to.
        """
        self.host = host
        self.port = port
        self.connected = False
        self.protocol = protocol.Protocol()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(constants.SOCKET_TIMEOUT)
        self.socket_lock = threading.Lock()
        self.packet_lock = threading.Lock()
        self.packet_queue = []
        self
