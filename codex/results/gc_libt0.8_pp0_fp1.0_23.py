import gc, weakref
from sys import stderr
from math import ceil

from .MyTestCase import MyTestCase

from . import c_test
from . import const
from . import python_test
from . import python_obj


# def _coverage(_):
#     # print('_coverage')
#     print(gc.collect())
#     c_test.report_coverage()


# atexit.register(_coverage)


class TestC(MyTestCase):
    def setUp(self):
        self.count = 2

    def test_all(self):
        # print('TestC.test_all')
        # print(gc.collect())
        # c_test.report_coverage()
        self.assertEqual(self.count, c_test.test_all(self.count))

    def test_Py_INCREF(self):
        self.assertEqual(self.count, c_test.test_Py_INCREF(self.count))

    def test_Py_XINCREF(self):
        self.assertEqual(self.
