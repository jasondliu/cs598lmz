import select
import socket
import sys
import time
import traceback

import pytest

from . import util

if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class Test(unittest.TestCase):

    def test_poll(self):
        poll = select.poll()
        self.assertRaises(NotImplementedError, poll.poll, 0)

    def test_select(self):
        self.assertRaises(NotImplementedError, select.select, [], [], [], 0)

    def test_select_exception(self):
        # Issue #7992: select() should not swallow arbitrary exceptions
        class EvilException(Exception):
            pass

        def evil_select(rlist, wlist, xlist, timeout=None):
            raise EvilException()

        oldselect = select.select
        select.select = evil_select
