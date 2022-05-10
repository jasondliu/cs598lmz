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

    def test_socket_server_with_ssl_and_cert_reqs(self):
        self.start_server(
            socket_server=True,
            ssl_context=util.get_ssl_context(cert_reqs=ssl.CERT_REQUIRED),
        )
        self.assert_server_started()

    def test_socket_server_with_ssl_and_cert_reqs_and_ca_certs(self):
        self.start_server(
            socket_server=True,
            ssl
