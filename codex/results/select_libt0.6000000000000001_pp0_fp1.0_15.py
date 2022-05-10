import select
import struct
import sys
import threading
import time
import traceback
import unittest

import common
import pyuv


TEST_PORT = 1234

class TCPError(Exception):
    pass


class TCPClient(object):
    def __init__(self, loop):
        self.loop = loop
        self.connected = False
        self.closed = False
        self.connect_cb_called = False
        self.shutdown_cb_called = False
        self.closed_cb_called = False
        self.connection = pyuv.TCP(loop)
        self.connection.connect((common.TEST_IPV4_ADDR, TEST_PORT), self.on_connect)

    def on_connect(self, handle, error):
        assert handle is self.connection
        self.connected = True
        self.connect_cb_called = True

    def shutdown(self):
        self.connection.shutdown(self.on_shutdown)

    def on_shutdown(self, handle):
        assert handle is self.connection
        self.shut
