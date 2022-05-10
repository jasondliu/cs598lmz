import gc, weakref, math
from tools.lib.loopback import Loopback
import tools.lib.log as log

class Bus(object):
    """
    A class representing a CAN bus.

    Attributes:
      name: The name of the bus.
      log_queue: The queue to be used for logging.
    """

    def __init__(self, name, log_queue):
        self.name = name
        self.log_queue = log_queue

        self.loopback = Loopback(self.log_queue)
        self.loopback.start()

    def __str__(self):
        return 'Bus(%s)' % (self.name)

    def __repr__(self):
        return str(self)

class BusSet(object):
    """
    A class representing a set of busses.

    Attributes:
      bus_list: The list of busses.
      log_queue: The queue to be used for logging.
    """

    def __init__(self, log_queue):
        self.bus_list = []
        self.log
