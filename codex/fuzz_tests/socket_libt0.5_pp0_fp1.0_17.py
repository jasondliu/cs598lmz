import socket
import sys
import time
import traceback

from multiprocessing import Process
from threading import Thread

from . import __version__ as _version
from . import _logging
from . import _utils

__author__ = "Domen Ipavec"
__copyright__ = "Copyright (c) 2015, Domen Ipavec"

class Server:
    """Tcp server.
    
    Parameters:
        address: address to listen on.
        handler: handler to call when a new connection is received.
        logger: logger to use, if not specified, a new one will be created.
        thread: if True, start a new thread for each connection.
        process: if True, start a new process for each connection.
        backlog: maximum length of the queue of pending connections.
        reuse_address: set SO_REUSEADDR on the socket.
        keep_alive: set SO_KEEPALIVE on the socket.
        timeout: timeout for accepting new connections.
        shutdown_timeout: timeout for shutdown.
        shutdown_graceful: if True, shutdown gracefully
