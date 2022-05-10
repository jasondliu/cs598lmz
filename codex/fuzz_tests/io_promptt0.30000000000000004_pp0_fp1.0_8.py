import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import tempfile
import functools
import contextlib
import pickle
import gc
import warnings
import random

from test import support
from test.support import import_helper
from test.support.script_helper import assert_python_ok

# Base class for testing io.RawIOBase.
# To test a concrete RawIO implementation, subclass this and override
# setUp(), tearDown(), and any abstract methods.

class BaseRawTests(unittest.TestCase):
    # Subclass must override
    def setUp(self):
        raise NotImplementedError

    # Subclass must override
    def tearDown(self):
        raise NotImplementedError

    # Subclass must override
    def _make_instance(self, *args, **kwargs):
        raise NotImplementedError

    def test_rawio_attributes(self):
        rawio = self._make_instance()
        self.assertEqual(rawio.mode
