import weakref

from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.internet.task import Clock
from twisted.internet import reactor

from vumi.tests.helpers import VumiTestCase
from vumi.tests.utils import LogCatcher
from vumi import log


class DummyWorker(object):
    """
    Dummy worker for testing.

    :type clock: :class:`twisted.internet.task.Clock`
    :type _transport: :class:`DummyTransport`
    """
    def __init__(self, config={}):
        self._config = config
        self._transport = None
        self.clock = Clock()

    def set_clock(self, clock):
        """Used for testing to set a clock for time related tests."""
        self.clock = clock

    def set_transport(self, transport):
        """
        Used for testing to set a transport for transport related tests.
        """
        self._transport = transport

    def get_transport_worker(self, worker_name):
        """

