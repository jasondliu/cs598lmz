import signal
# Test signal.setitimer(), which is used to schedule
# a callback from a python function and also, ultimately,
# to arrange for the killing of this process at the end
# of the test run.

import sys
import socket
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from SocketServer import TCPServer
from test import test_support
from unittest import TestCase, TestSuite, TestLoader


# Installs a SIGCHLD handler, so we must be careful not to
# accidentally call fork() before this is done.
#
# This is done in the setUp() method of the TestCase rather than in
# setUpModule() so that the test is able to check that the signal
# handler was actually installed.

class Test_install(TestCase):

    def setUp(self):
        self.old_alrm = signal.signal(signal.SIGALRM, self.sig_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alrm)

