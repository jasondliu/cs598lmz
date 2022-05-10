import weakref
import sys
import os

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TTransportException
from thrift.transport.THeaderTransport import THeaderTransport

from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.protocol.TJSONProtocol import TJSONProtocol
from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol

from thrift.Thrift import TApplicationException

from .exceptions import *

# This is a hack to make it easier to construct a transport
# from an open socket.
# TODO: submit a patch to thrift to add this to TTransport
class TSocketFromSocket(TSocket):
    def __init__(self, sock, unix_socket=False):
        self.sock = sock
        self.handle = sock.fileno()
        self.unix_socket = unix_socket
        self.__
