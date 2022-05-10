import select
# Test select.select: File obj.

import select
import unittest
from test import test_support
from test.script_helper import assert_python_ok, assert_python_failure
from test.script_helper import assert_python_exit_zero

from test.script_helper import argv_as_bytes
from test.script_helper import import_module

from sys import getrefcount

class SelectTestCase(unittest.TestCase):
    def setUp(self):
        self.evt, self.evt_args = test_support.threading_setup()

    def tearDown(self):
        test_support.threading_cleanup(*self.evt_args)

    def test_error_conditions(self):
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [1], 2, 3)
        self.assertRaises(TypeError, select.select, [1], [2], 3)
        self.assertRaises(TypeError, select
