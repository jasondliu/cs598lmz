import select
import socket
import sys
import traceback
from threading import Thread
from time import sleep

from . import __version__
from . import config
from . import log
from . import util


logger = log.get_logger(__name__)


class Server(object):
    def __init__(self, listen_port, listen_addr,
                 remote_port, remote_addr,
                 password, method, timeout=600,
                 fast_open=False, workers=1):
        self.listen_port = listen_port
        self.listen_addr = listen_addr
        self.remote_port = remote_port
        self.remote_addr = remote_addr
        self.password = password
        self.method = method
        self.timeout = timeout
        self.fast_open = fast_open
        self.workers = workers
        self.manager = None
        self.dns_resolver = AsyncResolver()
        self.fd_to_handlers = {}
        self.last_time = time.time()
        self.eventloop = Event
