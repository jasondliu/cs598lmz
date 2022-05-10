import threading
# Test threading daemon
from time import sleep
from random import randint
from datetime import datetime
from sys import stdout
from os import system

from lib.core import *
from lib.config import *
from lib.log import *
from lib.db import *
from lib.util import *

from lib.daemon import Daemon
from lib.daemon import DaemonThread

# Test threading daemon
def test_daemon():
    class TestThread(DaemonThread):
        def __init__(self, name, interval=1):
            DaemonThread.__init__(self, name, interval)
            self.interval = interval

        def run(self):
            while self.running:
                print('%s: %s' % (self.name, datetime.now()))
                sleep(self.interval)
            print('%s: %s' % (self.name, datetime.now()))

    class TestDaemon(Daemon):
        def __init__(self, name, interval=1):
            Daemon.__init__(self, name)
            self
