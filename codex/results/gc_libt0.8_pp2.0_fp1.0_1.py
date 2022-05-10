import gc, weakref
from datetime import datetime, timedelta
from twisted.internet.defer import Deferred
from twisted.internet import reactor, protocol
from twisted.internet.task import LoopingCall

from .util import dump, pp
from . import log
from . import archive
from . import api
from . import defs
from . import item
from . import monitor
from . import connection
from . import util
from . import net
from . import config

_missing = object()

class MonitorContext(object):
    def __init__(self, monitor, items):
        self.monitor = monitor
        self.items = items

    def __enter__(self):
        self.monitor.add_items(*self.items)

    def __exit__(self, exc_type, exc_value, traceback):
        self.monitor.remove_items(*self.items)

class _Monitor(object):
    def __init__(self):
        self.items = []
        self.log = log.logger('monitor.Monitor')
        self.log.info('monitor: init')
        self.
