import gc, weakref

from threading import Thread
from threading import current_thread

from time import time
from time import sleep
from time import clock
from random import randint

from multiprocessing import Queue
from multiprocessing import cpu_count

from Queue import Full
from Queue import Empty

from shared_data.logger import *


class Process_Monitor (Thread):
    """
    The Process_Monitor is used to monitor the status of
    threads and processes. This is done by having a
    single process monitor that periodically polls each
    thread or process in the system. It will also call
    the periodic function associated with each process
    that has been registered with the monitor.
    """

    def __init__ (self, config, check_period=1.0):
        """
        Initialize the monitor
        """
        super(Process_Monitor, self).__init__()
        self.name = 'Monitor'
        self.daemon = True
        self.setName(self.name)
        
        self.check_period = check_period
        self.config = config
