import io
# Test io.RawIOBase

import io
import socket
import sys
import unittest
import unittest.mock
from test import support
from test.support.script_helper import assert_python_ok

from contextlib import closing
from io import UnsupportedOperation

try:
    from multiprocessing import Process, Queue, Pipe
except ImportError:
    Process = Queue = Pipe = None


class io_tests(unittest.TestCase):
    def test_IOBase(self):
        # Make sure the ABC actually provides a useful isinstance check
        self.assertTrue(isinstance(self.IOCls(), io.IOBase),
                             '{}.__instancecheck__ not working'.format(self.IOCls()))

    def test_seek_read(self):
        data = 'Mary had a little lamb, little lamb, little lamb'
        io = self.IOCls(data)
        self.assertEqual(io.seekable(), False,
                         '{} should not be seekable by default'.format(self.IOCls))
        self.assertEqual
