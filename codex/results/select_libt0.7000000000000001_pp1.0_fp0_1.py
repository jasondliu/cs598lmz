import select
import socket
import sys
import traceback
from threading import Thread

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .utils import get_logger
from .configuration import Configuration

logger = get_logger(__name__)

class FTPThread(Thread):
    def __init__(self, server, port, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.server = server
        self.port = port

        self.shutdown = False
        self.restart = False

    def run(self):
        while not self.shutdown:
            try:
                self.server.serve_forever(timeout=1, blocking=False)
            except Exception as e:
                logger.error(e)

            if self.restart:
                self.restart = False
                self.shutdown = True

            time.sleep(1)

        self.server.close_all
