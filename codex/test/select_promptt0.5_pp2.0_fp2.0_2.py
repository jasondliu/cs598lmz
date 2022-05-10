import select
# Test select.select() on a socket

# This test is derived from test_select.py, but uses a socket instead
# of a pipe.  The server side of the socket is a thread that sends
# data to the client when it's ready.  This is a bit of a hack, but
# it means that we can test the client side of select() without
# having to worry about the server side blocking.

import os
import socket
import threading
import time
import unittest
from test.support import run_unittest
from test.support import TESTFN, find_unused_port

HOST = 'localhost'

class SocketReady(threading.Thread):
    """Thread that waits for a socket to be ready, then sends data"""

    def __init__(self, sock, writable, readable):
        threading.Thread.__init__(self)
        self.sock = sock
        self.writable = writable
        self.readable = readable
        self.finished = 0

    def run(self):
        # Wait for the socket to be ready
        print('thread waiting')
       
