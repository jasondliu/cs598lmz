import types
types.ClassType = type
from cStringIO import StringIO
import sys
import unittest

from . import test_support


class Test_run(unittest.TestCase):

    def test_run__initial_failure(self):
        result = unittest.TestResult()
        class BadTest(unittest.TestCase):
            def run(self, result):
                raise RuntimeError('run')
        test = BadTest('test')
        test.run(result)
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(result.errors[0][0], test)

    def test_run__subtests(self):
        result = unittest.TestResult()

        class Test(unittest.TestCase):
            def test(self):
                self.subTest().run(result)
                self.subTest().run(result)

        test = Test('test')
        test.run(result)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result
