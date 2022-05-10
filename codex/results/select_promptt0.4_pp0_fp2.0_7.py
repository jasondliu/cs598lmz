import select
# Test select.select()
#
# $Id: test_select.py,v 1.3 2007/04/15 00:42:25 jriehl Exp $

import unittest
import os
import sys
import time
import select
import threading
import Queue

from test import test_support

HOST = test_support.HOST

class ThreadedEchoServer(threading.Thread):

    def __init__(self, test_object, host=HOST, port=0):
        threading.Thread.__init__(self)
        self.daemon = True
        self.setDaemon(1)
        self.test_object = test_object
        self.host = host
        self.port = port
        self.ready_event = threading.Event()
        self.sock = None
        self.active = True

    def __getattr__(self, attr):
        # Proxy pass-through for most socket methods.
        return getattr(self.sock, attr)

    def run(self):
        self.sock = test_support.
