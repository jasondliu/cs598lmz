import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import utils


class TestFunctional(utils.TestCase):

    def test_functional(self):
        self.maxDiff = None
        self.start_server()
        self.start_client()
        self.assertEqual(self.client.stdout.read(), b'Hello, World!\n')
        self.assertEqual(self.client.stderr.read(), b'')
        self.assertEqual(self.client.returncode, 0)
        self.assertEqual(self.server.stdout.read(), b'')
        self.assertEqual(self.server.stderr.read(), b'')
        self.assertEqual(self.server.returncode, 0)

    def start_server(self):
        self.server = subprocess.Popen(
            [sys.executable, '-m', 'pytest_server', '--port', '0'],
            stdin=subprocess.PIPE,
