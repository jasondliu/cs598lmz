import select
import socket
import sys
import threading
import time
import traceback

import pytest

from tornado.escape import native_str
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.netutil import bind_sockets, Resolver, OverrideResolver
from tornado.tcpserver import TCPServer
from tornado.testing import AsyncTestCase, bind_unused_port, ExpectLog
from tornado.test.util import unittest, skipIfNonUnix, skipOnTravis


class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        self.stream = stream
        self.address = address
        self.stream.read_until_close(self._read_callback,
                                     streaming_callback=self._streaming_callback)

    def _streaming_callback(self, data):
        self.stream.write(data)

    def _read_callback(self, data):
        self.stream.close()


