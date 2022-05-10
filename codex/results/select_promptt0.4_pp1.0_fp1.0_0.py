import select
# Test select.select

# FIXME: This test is not very good.  It's hard to tell if select.select is
# working correctly.

import select
import socket
import sys
import time
import unittest

from test import support
from test.support import find_unused_port


@unittest.skipUnless(hasattr(select, 'poll'), 'poll not available')
class PollTests(unittest.TestCase):

    def test_poll(self):
        pollster = select.poll()
        fd = sys.stdin.fileno()
        pollster.register(fd, select.POLLIN)
        result = pollster.poll()
        self.assertEqual(result, [])

    def test_poll_timeout(self):
        pollster = select.poll()
        fd = sys.stdin.fileno()
        pollster.register(fd, select.POLLIN)
        result = pollster.poll(timeout=1e6)
        self.assertEqual(result, [])

    def test_poll_timeout_negative(self
