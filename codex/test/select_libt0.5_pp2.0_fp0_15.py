import select
import time
import sys
import os
import threading

from pyftpdlib import ftpserver
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from . import log
from . import exceptions
from . import settings

logger = log.get_logger(__name__)


class FTPHandler(FTPHandler):

    def on_connect(self):
        logger.debug('FTP client connected')

    def on_disconnect(self):
        logger.debug('FTP client disconnected')

    def on_login(self, username):
        logger.debug('FTP client logged in as %s', username)

    def on_login_failed(self, username, password):
        logger.debug('FTP client login failed for %s', username)

    def on_logout(self, username):
        logger.debug('FTP client logged out as %s', username)
