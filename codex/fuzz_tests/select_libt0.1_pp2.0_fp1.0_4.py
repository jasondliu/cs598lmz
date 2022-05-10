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

#------------------------------------------------------------------------------
# globals

_log = log.get_logger()

#------------------------------------------------------------------------------
# classes

class XLogViewerServer(xlogserver.XLogServer):
    """
    XLogViewerServer is a server that listens for connections from
    XLogViewer clients.
    """

    def __init__(self, port):
        """
        Constructor.

        @param port the port to listen on
        """
        super(XLogViewerServer, self).__init__(port)

        self._log_viewer = xlogviewer.XLogViewer()

    def _handle_client(self, client_sock):
        """
        Handle a client connection.

        @param client_sock the client socket
        """
       
