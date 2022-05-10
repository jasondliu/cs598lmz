import gc, weakref

from twisted.internet.protocol import DatagramProtocol as _DatagramProtocol
from twisted.internet.tcp import Client
from twisted.internet.error import CannotListenError
from twisted.python.runtime import platform
from twisted.internet import task
import errno

from zope.interface import implements

from foolscap.eventual import eventually
from foolscap.logging import  EVENTUAL_LEVEL
from foolscap.tokens import BananaError
from foolscap.interface import IFoolscapReceiver
from foolscap.ipb import negotiate_pb
from foolscap.banana import TokenType, TokenReader
from foolscap.banana import check_stream_type, smart_banana_decode, BananaFailure


class WireLoggerWrapper(object):
    """A wrapper for Foolscap's stream loggers, which records incoming and
    outgoing messages and sequences."""
    def __init__(self, streamlog):
        self._streamlog = streamlog
        self._streamlog_initialized = False
        self._our_side = None
        # Outgoing
