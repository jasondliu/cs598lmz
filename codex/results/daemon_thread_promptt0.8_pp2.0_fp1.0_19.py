import threading
# Test threading daemon

import time
from multiprocessing import Process
from util import *

import signal
from time import sleep


class DaemonTest(Daemon):
    def __init__(self, test_name, timeout, signal_type, signal_handler_type, signal_handler_func):
        Daemon.__init__(self, test_name, timeout)
        self.signal_type = signal_type
        self.signal_handler_type = signal_handler_type
        self.signal_handler_func = signal_handler_func

    def signal_handler_1(self):
        print("signal handler 1")
        return self.signal_handler_func()

    def signal_handler_2(self):
        print("signal handler 2")
        return self.signal_handler_func()

    def signal_handler_3(self):
        print("signal handler 3")
        return self.signal_handler_func()

    def signal_handler_4(self):
        print("signal handler 4")
        return self.signal_handler_func()
