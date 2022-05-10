import select
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
from . import xlogserver
from . import xlogviewer_pb2

_logger = log.get_logger(__name__)


class XlogViewerServer(xlogserver.XlogServer):
    def __init__(self, config_file):
        super(XlogViewerServer, self).__init__(config_file)
        self.xlog_viewer = xlogviewer.XlogViewer(self.config)
        self.xlog_viewer.start()

    def _handle_request(self, request):
        if request.type == xlogviewer_pb2.XlogViewerRequest.GET_XLOG:
            return self._handle_get_xlog(request)
        elif request.type == xlogviewer_pb2.XlogViewerRequest.GET_XLOG_LIST:

