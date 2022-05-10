import weakref
from time import time
import re

from threading import Thread, Lock, Timer
import logging
logger = logging.getLogger('utils.timer')

class RepeatingTimer(Thread):
    """
    Thread that executes events at the desired intervals.

    The timer should be started in a separate thread.
    The events are kept around until they are explicitly stopped.
    """

    def __init__(self, name=None):
        Thread.__init__(self, name=name or 'Timer' + Thread.name)

        self.running = False

        self.events = weakref.WeakValueDictionary() # {event_id : TestEvent, ...}

        self.lock = Lock()
        self.monitor = Lock()

    def start(self):
        """
        Start the timer thread.
        """

        Thread.start(self)
        logger.debug('started')

    def stop(self):
        """
        Stop the timer thread.
        """

        self.running = False
        self.monitor.acquire() # release by run()

        # stop events
       
