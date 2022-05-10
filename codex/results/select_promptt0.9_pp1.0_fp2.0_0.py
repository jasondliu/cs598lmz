import select
# Test select.select() and select.pselect() timeout argument with
# struct.pack_into().
import struct
import time
import unittest

class SelectTimeoutTest(unittest.TestCase):

    def assertRaisesErrno(self, cls, errno, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except cls as e:
            self.assertEqual(e.errno, errno)
        else:
            self.fail('%s not raised' % cls)

    def test_select_timeout(self):
        # select() should work with a zero-length struct
        self.assertEqual(select.select([], [], [], 0.0),
                         ([], [], []))

    def test_select_pack_into_timeout(self):
        # select() should work with a struct packed into a buffer
        buf = bytearray(struct.calcsize('llll'))
        struct.pack_into('llll', buf, 0, 0, 0, 0, 0)
        self.
