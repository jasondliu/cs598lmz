import _struct

from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


class Sender(DatagramProtocol):
    def startProtocol(self):
        # Called when transport is connected
        pass

    def stopProtocol(self):
        # Called when transport is disconnected
        pass

