import io
# Test io.RawIOBase

import sys
import unittest
import weakref
import contextlib

from test import support


class MyRawIO(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True


class BadMetaRawIO(MyRawIO):

    def __init__(self, name):
        self.name = name


class MockUnseekableIO(io.RawIOBase):
    """A mock file-like object that isn't seekable, for testing __next__.

    The file-like object should have a read() method that accepts n as an
    argument, and returns up to n characters, or "".
    """

    def __init__(self, read_mock, readable=True):
        self._read_mock = read_mock
        self._readable = readable

    def readable(self):
        return self._readable

    def readinto(self, b):
        data = self._read_mock(len(b))
        n = len(data
