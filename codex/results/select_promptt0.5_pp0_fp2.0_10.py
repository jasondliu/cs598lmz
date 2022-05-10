import select
# Test select.select() with a readable pipe and a writable pipe.
import os
import select
import sys
import time
import unittest


class SelectTest(unittest.TestCase):

    def test_select(self):
        r, w = os.pipe()
        self.addCleanup(os.close, r)
        self.addCleanup(os.close, w)
        for i in range(5):
            t1 = time.monotonic()
            rfds, wfds, xfds = select.select([r], [w], [], 2.0)
            t2 = time.monotonic()
            self.assertLess(t2 - t1, 2.0, 'blocking select took %s' % (t2 - t1))
            self.assertEqual(rfds, [r])
            self.assertEqual(wfds, [w])
            self.assertEqual(xfds, [])
            os.write(w, b'x')
            self.assertEqual(os.read(r, 1), b'x')


