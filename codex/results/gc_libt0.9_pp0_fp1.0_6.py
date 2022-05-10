import gc, weakref
from weakref import WeakValueDictionary
from weakref import ref

import e_dbus_base
import e_dbus_signal

from decorators_ import threaded

import testutils
import types

class CustomType(object):
    def __init__(self, name):
        self.name = name
        logger.debug('%s created' % self.name)

    def __del__(self):
        logger.debug('%s deleted' % self.name)


class FrameworkTest(unittest.TestCase):
    """The base class for the testcases.

    """
    def setUp(self):
        self.bus = dbus.SessionBus()
        self.busname = dbus.service.BusName(testutils.unique_name(), self.bus)
        self.loop = gobject.MainLoop()

    def tearDown(self):
        del self.bus
        del self.busname
        del self.loop

    def run_loop(self, nloops = 1):
        while nloops:
            self.loop.run
