import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import utils
from . import version
from . import xlog
from . import xlogviewer
from . import xlogserver
from . import xlogserver_pb2
from . import xlogserver_pb2_grpc
from . import xlogviewer_pb2
from . import xlogviewer_pb2_grpc

_logger = log.get_logger(__name__)


class XlogServer(xlogserver_pb2_grpc.XlogServerServicer):
    def __init__(self, config):
        self._config = config
        self._xlog_server = xlogserver.XlogServer(config)
        self._xlog_server.start()

    def GetXlog(self, request, context):
        return self._xlog_server.get_xlog(request.xid)

    def GetXlogs(self, request
