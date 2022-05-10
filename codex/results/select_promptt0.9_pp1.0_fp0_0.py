import select
# Test select.select using select.epoll.

import os
import socket
import select_helpers
from test import support

support.import_module('twisted.internet.pollreactor')
from twisted.internet.pollreactor import PollReactor

#
# NOTE: If a test triggers an exception, that's OK. The point of these tests is
# to verify the use of select does not break the underlying operation.
#

class Tests:

    def __init__(self, reactor, family):
        self.reactor = reactor
        self.family = family

    def create_server(self, sa):
        s = self.family.socket()
        s.bind(sa)
        s.listen(5)
        self.reactor.addReader(s)
        return s

    def create_pair(self):
        s, c = self.family.socketpair()
        self.reactor.addReader(s)
        self.reactor.addWriter(c)
        return s, c

    def test_accept(self):
        s = self.create_server(('localhost
