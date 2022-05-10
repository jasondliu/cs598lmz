import io
# Test io.RawIOBase.readahead method
# http://bugs.python.org/issue18288

from test import support
from io import RawIOBase
import unittest
from io import BytesIO
from io import SEEK_CUR
import _pyio as pyio
from sys import byteorder
from _io import DEFAULT_BUFFER_SIZE
import sys
from test import script_helper

from _io import IOBase
from _io import FileIO
from _io import BufferedReader
from _io import BufferedWriter
from _io import BufferedRWPair
import os

from os import fdopen, dup, close

from test import script_helper
from test.script_helper import assert_python_ok



# A mock raw file interface that raises an exception on all operations.
class MockRawIO(RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        raise OSError

    def readall(self):
