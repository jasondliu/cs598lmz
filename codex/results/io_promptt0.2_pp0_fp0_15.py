import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import pickle
import struct
import tempfile
import threading
import time
import warnings
import subprocess
import errno
import select
import socket
import functools

from test import support

# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write,
