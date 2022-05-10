import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import xlog
from . import xlogviewer
from . import xlogviewer_pb2
from . import xlogviewer_rpc
from . import xlogviewer_rpc_pb2
from . import xlogviewer_rpc_pb2_grpc

_logger = log.get_logger(__name__)


class XlogViewerServer(xlogviewer_rpc_pb2_grpc.XlogViewerServicer):
    def __init__(self, xlog_viewer):
        self._xlog_viewer = xlog_viewer

    def GetXlog(self, request, context):
        try:
            xlog = self._xlog_viewer.get_xlog(request.xid)
            return xlogviewer_rpc_pb2.GetXlogResponse(xlog=xlog)
        except xlogviewer.XlogNot
