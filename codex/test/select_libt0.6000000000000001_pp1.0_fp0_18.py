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

