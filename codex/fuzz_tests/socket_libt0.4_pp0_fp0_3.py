import socket
import struct
import time

from lib import common
from lib import config
from lib import connection
from lib import exceptions
from lib import helpers
from lib import packet
from lib import protocol
from lib import relay
from lib import socks

log = logging.getLogger(__name__)


class Server(connection.Connection):
    """
    Server side of a connection.
    """

    def __init__(self, *args, **kwargs):
        super(Server, self).__init__(*args, **kwargs)

        self.relay = None
        self.client = None
        self.protocol = None
        self.socks_request = None

        self.state = common.State()

    def initialize(self):
        """
        Perform post-construction initialization.

        This method should be called after the connection is constructed.
        """

        self.protocol = protocol.Protocol(self.state)

        self.protocol.server_handshake_completed.subscribe(self._on_handshake_completed)
        self.protocol.server_authent
