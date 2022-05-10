import select
# Test select.select with write-only and non-blocking sockets.
import socket
import sys
import threading
import time
import unittest
from test import support
import warnings

if hasattr(select, 'poll'):
    def get_readers_and_writers():
        """Helper for test_select.  Returns (readers, writers)."""
        # We've got a few readers and writers, all connected to the
        # same port on localhost.
        port = support.bind_port(socket.socket())
        readers = []
        writers = []
        for i in range(5):
            s = socket.socket()
            s.bind(('localhost', port))
            s.listen(1)
            readers.append(s)
        for i in range(3):
            s = socket.socket()
            s.connect(('localhost', port))
            writers.append(s)
        readers_and_writers = readers[:]
        readers_and_writers.extend(writers)
        return readers, writers, readers_and_writers
class SelectTestCase(unittest.Test
