import socket
import sys
import threading
import time

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver

from . import constants
from . import errors
from . import log
from . import settings
from . import utils
from . import version
from .protocol import Protocol


class ClientFactory(ClientFactory):
    """Factory for creating a client."""

    def __init__(self, client):
        """Initialize the factory."""
        self.client = client

    def buildProtocol(self, addr):
        """Build the protocol."""
        self.client.protocol = Protocol()
        self.client.protocol.factory = self
        return self.client.protocol

    def clientConnectionLost(self, connector, reason):
        """Called when the connection is lost."""
        self.client.on_disconnect()

    def clientConnectionFailed(self, connector, reason):
        """Called when the connection failed."""
        self.client.on_disconnect()


