import select
# Test select.select implementation, coverage 17.07%

import sys
import unittest
from test import support
from collections import namedtuple

try:
    select.kqueue
except AttributeError:
    raise unittest.SkipTest("Test requires kqueue(2) support")

class KqueueTests(unittest.TestCase):
    def setUp(self):
        self.kq = select.kqueue()

    def tearDown(self):
        self.kq.close()

    def test_error(self):
        # Issue #8280: selecting with a huge timeout must raise a ValueError
        self.assertRaises(ValueError, self.kq.control, None, 10, 0)

    # Tests

    def test_kevent_happened(self):
        # detecting a write event
        r, w, x = select.select([], [self.kq], [])
        self.assertEqual(w, [self.kq])

    def test_control(self):
        # controlling an event
        dummy = open(support.TESTFN,
