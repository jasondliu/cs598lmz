import socket
import time

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from . import config
from . import log
from . import util
from . import version

logger = log.get_logger(__name__)


class FTPServerThread(threading.Thread):
    """
    FTP server thread.
    """
    def __init__(self, ftp_server):
        super(FTPServerThread, self).__init__()
        self.ftp_server = ftp_server

    def run(self):
        self.ftp_server.serve_forever()

    def stop(self):
        self.ftp_server.close_all()


class FTPServerHandler(FTPHandler):
    """
    FTP server handler.
    """
    def on_connect(self):
        """
        Called when client connects.
        """
