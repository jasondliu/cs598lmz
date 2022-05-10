import gc, weakref

from twisted.internet import defer
from twisted.python import failure
from twisted.trial.unittest import TestCase
from twisted.python.util import unsignedID
from twisted.python.compat import nativeString
from twisted.python.components import registerAdapter
from twisted.web.http_headers import Headers
from twisted.web.http import datetimeToString, datetimeToLogString
from twisted.web.client import Agent, _HTTP11ClientFactory, ResponseDone
from twisted.web.server import Site, NOT_DONE_YET
from twisted.test.test_web import DummyChannel
from twisted.web.test.test_web import DummyRequest
from twisted.web.test.test_webclient import FakeTransport
from twisted.test.proto_helpers import StringTransport
from twisted.web.http_headers import Headers
from twisted.web.client import _HTTP11ClientFactory
from twisted.web.resource import Resource
from twisted.web.test.test_web import DummyChannel


class WebClientTestCase(TestCase):
    def setUp(self):
        self.
