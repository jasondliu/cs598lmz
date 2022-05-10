import socket
# Test socket.if_indextoname()
import sys
from test import support, socket_helper
import unittest
from unittest import mock
import errno
from io import BytesIO
import contextlib
import gc
import os
import re
import shutil
import subprocess
import tempfile
import time
import warnings


class SocketTCPTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = support.bind_port(self.serv)
        self.serv.listen(1)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", self.port))
        return sock

    def testTimeoutDefault(self):
        # Default timeout should be None.
        self.assertIsNone(socket.getdefaulttimeout())

