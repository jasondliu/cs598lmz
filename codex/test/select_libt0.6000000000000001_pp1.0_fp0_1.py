import select
import signal
import sys
import threading
import time

import pytest

from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.netutil import bind_sockets
from tornado.platform.auto import set_close_exec, Waker
from tornado.testing import AsyncTestCase, bind_unused_port, ExpectLog
from tornado.test.util import unittest


class TestIOLoop(AsyncTestCase):
    def setUp(self):
        super(TestIOLoop, self).setUp()
        self.io_loop = IOLoop()

    def tearDown(self):
        self.io_loop.close()
        super(TestIOLoop, self).tearDown()

    def get_new_ioloop(self):
        return IOLoop()
