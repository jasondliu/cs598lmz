import select
# Test select.select.

import select
import time

class TestSelect (unittest.TestCase):

    def setUp(self):
        self.r, self.w = os.pipe()
        self.test_support.unlink(test_support.TESTFN)

    def tearDown(self):
        os.close(self.r)
        os.close(self.w)
        self.test_support.unlink(test_support.TESTFN)

    def test_error_conditions(self):
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [1], 2, 3)
        self.assertRaises(TypeError, select.select, [], [2], 3)
        self.assertRaises(TypeError, select.select, [], [], [3])
        self.assertRaises(TypeError, select.select, 1, [2], [3])
