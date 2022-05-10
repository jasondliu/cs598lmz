import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import util


class TestSocket(util.TestServer):
    def test_socket(self):
        self.assertEqual(self.client.socket.fileno(), self.client.fileno())

    def test_socket_close(self):
        self.client.socket.close()
        self.assertEqual(self.client.socket.fileno(), -1)

    def test_socket_closed(self):
        self.client.close()
        with pytest.raises(ValueError):
            self.client.socket.close()

    def test_socket_closed_fileno(self):
        self.client.close()
        with pytest.raises(ValueError):
            self.client.socket.fileno()

    def test_socket_closed_recv(self):
        self.client.close()
        with pytest.raises(ValueError):
            self.client.socket.recv(1)

    def test_socket_closed_
