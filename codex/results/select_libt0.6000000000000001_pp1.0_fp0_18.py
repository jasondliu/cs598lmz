import select
import socket
import sys
import time
import traceback

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.internet.task import LoopingCall

from .. import constants
from .. import protocol
from .. import reactor as zope_reactor


class ZopeReactor(object):
    """Reactor implementation that uses zope.interface.

    It is also possible to use the reactor from Twisted, but this requires
    adapting the Twisted reactor to the zope.interface interface.

    """

    def listenTCP(self, port, factory, interface='', backlog=50):
        """Listens to a TCP port.

        :param port: port number to listen to
        :param factory: :class:`~.ClientFactory` instance
        :param interface: interface to listen to
        :param backlog: maximum number of queued connections

        :returns: :class:`~.ZopePort` instance

        """
        return ZopePort(port, factory, interface, backlog)

    def listenUNIX(self, address, factory, backlog=50):
        """
