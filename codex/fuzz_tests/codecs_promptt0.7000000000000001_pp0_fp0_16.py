import codecs
# Test codecs.register_error()

import sys
import os
from test.support import run_unittest, findfile, TESTFN, rmtree, unlink
import unittest

import test_support

class TestRegistry(unittest.TestCase):

    def setUp(self):
        self.test_file = TESTFN
        f = open(self.test_file, "w")
        try:
            f.write("\xa1\xa2\x00")
        finally:
            f.close()

    def tearDown(self):
        unlink(self.test_file)

    def test_strict(self):
        self.assertRaises(UnicodeError, codecs.open,
                          self.test_file, "r", "latin-1",
                          "strict")

    def test_ignore(self):
        f = codecs.open(self.test_file, "r", "latin-1", "ignore")
        try:
            got = f.read()
        finally:
            f.close()
        self.assert
