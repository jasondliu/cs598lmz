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

    def __str__(self):
        return '<Device %s>' % self.serial

    #
    # State
    #
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        with self.__state_lock:
            self.__state = value

    #
    # ADB
    #
    def start_server(self):
        """
        Start the adb server.
        """
        utils.run_adb(['start-server'])

    def kill_server(self):

