import select
import time
import sys
import os

from . import utils

class Device(object):
    def __init__(self, serial=None,
                       verbose=False,
                       timeout=10):
        """
        Initialize an ADBServer object.
        """
        self.serial = serial

        self.verbose = verbose
        self.timeout = timeout

        self.__state = None
        self.__state_lock = threading.Lock()
