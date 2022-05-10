import socket
# Test socket.if_indextoname()
import sys
import time
import unittest

from tornado.testing import bind_unused_port, gen_test

from tornado import gen
from tornado.iostream import IOStream
from tornado.netutil import Resolver, add_accept_handler, add_reuse_addr
from tornado.netutil import bind_sockets, bind_sockets_with_backlog
from tornado.netutil import ssl_wrap_socket, ssl_match_hostname
from tornado.netutil import is_valid_ip
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.test.util import unittest, skipOnTravis, skipIfNonUnix
from tornado.testing import AsyncHTTPTestCase, AsyncTestCase, LogTrapTestCase
from tornado.testing import bind_unused_port, unused_port


class NetUtilTest(unittest.TestCase):
    def test_is_valid_ip(self):
        self.assertTrue(is_valid_ip("127.0.0.1"))
        self.assertFalse(is_valid_ip("
