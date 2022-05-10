import select
import sys
import time

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.protocols.basic import LineReceiver

from . import constants
from . import util
from . import xor
from . import exceptions
from . import log

from . import protocol
from . import protocol_pb2

from .log import get_logger

class ProtocolError(Exception):
    pass

class Client(protocol.Protocol):
    def __init__(self, factory):
        protocol.Protocol.__init__(self)
        self.factory = factory
        self.log = get_logger(self.__class__.__name__)

    def connectionMade(self):
        self.log.debug("connection made")
        self.factory.client = self
        self.factory.connector.connect_succeeded()

