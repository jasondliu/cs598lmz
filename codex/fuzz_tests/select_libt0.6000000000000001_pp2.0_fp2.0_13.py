import select
import socket
import sys
import time
import datetime
from subprocess import Popen, PIPE
from threading import Thread

from . import common
from . import utils
from . import console
from . import server
from . import client
from . import v3_server
from . import v3_client
from . import v3_server_ext

from . import logger

log = logger.Logger('socks.log', logger.Logger.DEBUG)

class Socks5Server(server.ThreadingTCPServer):
    """
    Socks5 Server
    """
    def __init__(self, server_address, RequestHandlerClass, config, bind_and_activate=True):
        server.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.config = config
        self.clients = {}
        self.client_count = 0
        self.client_id = 0

    def add_client(self, client):
        """
        Add client to clients dict
        """
        self
