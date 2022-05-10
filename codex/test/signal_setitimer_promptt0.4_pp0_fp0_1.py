import signal
# Test signal.setitimer()
#
# Author: Pearu Peterson, March 2002
#

import unittest
import os
import time
import sys
from test import test_support

class TestSetitimer(unittest.TestCase):

    def setUp(self):
        self.sigalrm = signal.SIGALRM
        self.sigterm = signal.SIGTERM
        self.sigint = signal.SIGINT
        self.sigusr1 = signal.SIGUSR1
        self.sigusr2 = signal.SIGUSR2
        self.sigcont = signal.SIGCONT
        self.sigchld = signal.SIGCHLD
        self.sigio = signal.SIGIO
        self.sigwinch = signal.SIGWINCH
        self.sigvtalrm = signal.SIGVTALRM
        self.sigprof = signal.SIGPROF
        self.sigpoll = signal.SIGPOLL
        self.sigstkfl = signal.SIGSTKFLT
        self
