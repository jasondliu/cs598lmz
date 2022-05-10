import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import utils
from . import version
from . import xlog
from . import xlog_pb2
from . import xlog_pb2_grpc
from . import xlog_pb2_twisted
from . import xlog_pb2_twisted_grpc

_logger = log.get_logger(__name__)


class XlogStub(xlog_pb2_grpc.XlogStub):
    def __init__(self, channel, timeout=None):
        super(XlogStub, self).__init__(channel)
        self.timeout = timeout

    def _wrap_unary_unary(self, method_descriptor, request, timeout=None):
        if timeout is None:
            timeout = self.timeout
