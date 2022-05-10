import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util
from . import x11

logger = log.get_logger(__name__)


class Connection(object):
    """
    A connection to a remote host.

    This class is a wrapper around a socket. It handles sending and receiving
    messages, and automatically reconnects if the connection is lost.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.lock = threading.Lock()
        self.read_thread = None
        self.read_thread_stop = threading.Event()
        self.read_thread_stop.set()
        self.read_thread_error = None
        self.write_thread = None
        self.write_thread_stop = threading.Event()
        self.write_thread_stop.set()
        self.write_thread_error = None
        self.write_queue = queue.Queue()
