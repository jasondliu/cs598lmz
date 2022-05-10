import select
# Test select.select for Linux, FreeBSD and Solaris.
import socket
import sys
import time
import unittest
from test import support
from test.support import TESTFN, run_with_locale, requires_mac_ver
from importlib import util as importutil
thread = importutil.import_module('_thread')
threading = importutil.import_module('threading')
# Skip this test if there is no threading.
threading.Thread  # Create and release lock.
import weakref
import os


@unittest.skipUnless(support.is_resource_enabled('network'), 'network')
class SelectTestCase(unittest.TestCase):
    """On Mac OS, select() only works on sockets; on Windows it works on
    sockets, pipes, and files."""

    def safe_close(self, s):
        if not s:
            return
        try:
            s.close()
        except OSError:
            pass

    def safe_closes(self, *args):
        for s in args:
            self.safe_close(s)

    def set
