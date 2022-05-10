import threading
threading._DummyThread._Thread__stop = lambda x: 42

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from datetime import datetime
from time import time


class SibylClientUdpBinProtocol(DatagramProtocol):
    """
        The class implementing the Sibyl UDP binary client protocol.  It has
        the following attributes:

        .. attribute:: proxy

            The reference to the SibylCientProxy (instance of the
            :py:class:`~sibyl.main.sibyl_client_proxy.SibylClientProxy` class).

            .. warning::
                All interactions between the client protocol and the user
                interface *must* go through the SibylClientProxy.  In other
                words you must call one of the methods of
                :py:class:`~sibyl.main.sibyl_client_proxy.SibylClientProxy` whenever
                you would like the user interface to do something.

        .. attribute:: serverAddress

            The address of the server.

        .. attribute:: serverPort

           
