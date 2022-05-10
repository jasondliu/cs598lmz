import codecs
# Test codecs.register_error()
import os
# Test os.umask()
import random
# Test random.seed()
import re
# Test re.ASCII, re.DEBUG, re.UNICODE, re.VERBOSE
import ssl
# Test ssl.*
import sys
# Test sys.getdefaultencoding(), sys.settrace(), sys.setprofile()
import threading
# Test threading.stack_size()
import time
# Test time.tzset()
import traceback
# Test traceback.format_exception()
import unittest
# Test unittest.TestCase.debug()
import warnings
# Test warnings.catch_warnings(), warnings.filterwarnings()


class TestInitialization(unittest.TestCase):
    def test_warnings(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            warnings.filterwarnings("ignore", "foo")
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, UserWarning))
