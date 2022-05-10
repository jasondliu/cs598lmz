import select
# Test select.select().

import unittest
from test import support
from test.support import import_module
select = import_module('select')


class SelectTestCase(unittest.TestCase):
    def setUp(self):
        self.r, self.w = socket.socketpair()

    def tearDown(self):
        self.r.close()
        self.w.close()

    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, [self.r], [], [], -1)
        self.assertRaises(TypeError, select.select, [self.r], [], [], 0, None)

    def test_read(self):
        data = b'x'
        n = self.w.send(data)
        fd_r, fd_w, fd_x = select.select([self.r], [], [], 1)
        self.assertFalse(fd_w)
        self.assertFalse(fd_x)
