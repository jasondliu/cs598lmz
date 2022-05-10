import codecs
# Test codecs.register_error('ignore')

import os
import sys
import time
import traceback
import types
import warnings

import unittest
from test import support
from test.support import TESTFN, run_unittest, unlink, import_module

# Skip tests if _multibytecodec isn't available.
_multibytecodec = import_module('_multibytecodec')

def force_str(s):
    if isinstance(s, bytes):
        return s.decode('ascii')
    return s

def force_bytes(s):
    if isinstance(s, str):
        return s.encode('ascii')
    return s

class TestBase:
    encoding = 'test'
    tstring = {
        'str': 'abc',
        'bytes': b'abc',
        'errorhandler': 'strict',
    }

    def setUp(self):
        self.errors = []
        self.errorhandler = None
        self.encoding = self.encoding
        self.tstring = self.
