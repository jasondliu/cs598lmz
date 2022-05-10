import weakref

from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from dnsagent.common.utils import log
from dnsagent.common.utils import utils

LOG = log.get_logger(__name__)


class Ticker(object):
    def __init__(self, seconds, callback, start=True):
        self.cb = callback
        self.loopingcall = LoopingCall(self.cb)
        self.loopingcall.start(seconds, now=start)

    def stop(self):
        self.loopingcall.stop()


class Dispatcher(object):
    '''Dispatcher for RPC messages.'''

    def __init__(self):
        self.targets = {}
        self.sources = {}
        self.ticker = None

    def register_target(self, target, callback):
        self.targets[target] = callback

    def register_source(self, source, callback):
        self.sources[source] = callback

    def register_ticker(self, seconds,
