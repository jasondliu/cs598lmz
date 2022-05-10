import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import util


class TestSocket(util.TestServer):
    def test_socket_server(self):
        self.start_server(socket_server=True)
        self.assert_server_started()

    def test_socket_server_with_ssl(self):
        self.start_server(socket_server=True, ssl_context=util.get_ssl_context())
        self.assert_server_started()
