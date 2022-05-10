import select
import socket
import sys
import time
import types
import unittest

from .. import utils
from .. import compat
from .. import errors
from .. import event
from .. import protocol
from .. import transport
from .. import futures
from .. import core
from .. import protocols
from .. import tasks
from .. import _base_events
from .. import _core


class EventLoopMixin:

    def create_server(self, protocol_factory, **kwds):
        raise NotImplementedError

    def run_until_complete(self, future):
        raise NotImplementedError

    def time(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def test_create_server_sock(self):
        loop = self.create_server_sock = self.create_server(protocols.Protocol)
        self.addCleanup(loop.close)
        host, port = utils.find_unused_port()
        server = loop.create_server(protocol_factory=protocol_
