import weakref

from twisted.internet import defer
from twisted.internet.task import LoopingCall

from . import settings
from .error import InvalidOperation
from .util import log, log_err
from .protocol import Message, MessageType, MessageError, MessageTypeError
from .serialization import serialize_message, deserialize_message
from . import __version__

class Connection(object):
    """
    This class is an implementation of the connection between a client and a
    server. It is a simple interface that can be used to send and receive
    messages between the two.
    """
    def __init__(self, peer, protocol, server=False):
        """
        Initialize a new connection.

        @param peer:
            The peer associated with this connection.
        @param protocol:
            The protocol used to send and receive messages.
        @param server:
            True if this is a server connection.
        """
        self.peer = peer
        self.protocol = protocol
        self.server = server

        # This is a hack to work around the fact that the protocol is currently
        #
