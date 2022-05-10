import select
# Test select.select

import unittest
import select
import os

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, [], [], [], -1)
        self.assertRaises(TypeError, select.select, 17, [], [], 0)
        self.assertRaises(TypeError, select.select, [], 17, [], 0)
        self.assertRaises(TypeError, select.select, [], [], 17, 0)
        self.assertRaises(TypeError, select.select, [], [], [], "foo")

    def test_returned_list_identity(self):
        # Check that the lists returned by select() are distinct
        r, w, x = select.select([], [], [], 0)
        self.assertNotEqual(r, w)
        self.assertNotEqual(r, x)
