import io
# Test io.RawIOBase

import unittest

import os
import sys
import tempfile
import io
import time
import errno
import _thread
import pickle
import contextlib

from test import test_support
from test import script_helper

try:
    import threading
except ImportError:
    threading = None

# Test the io.RawIOBase implementation of the RawIOBase abstract class.

class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        # Base classes for test cases
        class TestRawIO(io.RawIOBase):
            def __init__(self, read_stack, write_stack,
                         seek_stack, readinto_stack):
                self.read_stack = read_stack
                self.write_stack = write_stack
                self.seek_stack = seek_stack
                self.readinto_stack = readinto_stack
                self.closed = False
            def read(self, n=-1):
                if not self.read_stack:
                    raise IndexError
                if n == -1:
                   
