import select
# Test select.select() on a socket.

import unittest
import socket
import select
import threading
import errno
import sys

from test.support import (
    TESTFN, reap_children, socket_helper, get_unused_port, bind_port,
    run_with_tz, HOST, unlink, find_unused_port, find_unused_port
)

HOST = 'localhost'
MSG = b'Michael Gilfix was here\n'

class ThreadedTCPServer(object):
    """Class to run a simple single-threaded threaded TCP server"""

    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_shut_down = threading.Event()
        self.is_shut_down.clear()
        self.shutdown_request = False

    def server_bind(self):
        self.socket.
