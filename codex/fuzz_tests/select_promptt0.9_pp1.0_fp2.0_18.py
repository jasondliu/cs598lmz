import select
# Test select.select() is non-blocking
import signal
# Test that SIG_IGN doesn't hide exception in signal handler
import sys
# Test sys.exit() only quits the current thread
import threading
import time
import unittest
from test.fork_wait import ForkWait


class TestBasicOps(unittest.TestCase):

    def test_various_ops(self):

        class info:

            def __init__(self):
                self.x = 'foo'


        i = info()
        nm = 'x'
        exec('%s = %d' % (nm, 7), globals(), i.__dict__)
        self.assertEqual(i.x, 7)
        exec('%s = %d' % (nm, 8), i.__dict__)
        self.assertEqual(i.x, 8)
        exec('%s = %d' % (nm, 9), {}, i.__dict__)
        self.assertEqual(i.x, 9)
        exec('%s = %d' % (nm, 10))
        self
