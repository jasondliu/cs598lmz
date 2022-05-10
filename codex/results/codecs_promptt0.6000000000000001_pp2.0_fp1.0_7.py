import codecs
# Test codecs.register_error()
import copy
import getopt
import glob
import imp
import inspect
import io
import linecache
import marshal
import math
import ntpath
import os
import re
import struct
import sys
import time
import unittest
import unittest.mock
import warnings
import zipimport

from test import support
from test import script_helper
from test.support import TESTFN, run_unittest


class ExceptionTests(unittest.TestCase):

    def testRaisingStrings(self):
        # Raising a string should be deprecated, but not cause errors.
        with support.check_warnings(('deprecated', DeprecationWarning)):
            try:
                raise 'hello world'
            except TypeError:
                raise self.failureException('raising a string should not '
                                            'cause an error')

            try:
                raise ''
            except TypeError:
                raise self.failureException('raising an empty string should '
                                            'not cause an error')

    def test_instantiation(self):
        # Test
