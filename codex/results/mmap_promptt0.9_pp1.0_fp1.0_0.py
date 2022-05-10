import mmap
# Test mmap.mmap(0,1,prot=mmap.PROT_READ)

from functools import reduce
import itertools
from collections import namedtuple
from operator import or_
from itertools import chain
from itertools import takewhile
from itertools import repeat
from multiprocessing import Queue

from pytypes import Runnable


from execution.simulator import Event, Timestamp


class EventQueueProcess(Runnable):
    """
        I am a parallel process which contains a queue of Events goint to be simulated.
        TODO
    """
    def __init__(self, kernel, events, name = "EventQueue Process"):
        self.events = sorted(events, key = lambda e: e.timestamp)
        self.kernel = kernel
        self.queue = Queue()
        super(EventQueueProcess, self).__init__(name)

    def simulate_next_event(self, proc):
        event = self.queue.get()
        ts = Timestamp.getCurrentTime()
        if ts < event.timestamp:
            # sleep until
