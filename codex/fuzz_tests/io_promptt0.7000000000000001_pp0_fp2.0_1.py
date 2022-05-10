import io
# Test io.RawIOBase().readinto1() method

import unittest

from test import support
from test.support import import_module


class MockRawIO(io.RawIOBase):
    def __init__(self, read_data):
        self._read_data = read_data
        self._read_buffer = bytearray()
        self._read_offset = 0
        self._write_data = bytearray()
        self._write_buffer = bytearray()
        self._write_offset = 0
        self._seek_position = 0

    def readinto(self, b):
        read_size = min(len(self._read_data) - self._read_offset, len(b))
        b[:read_size] = self._read_data[self._read_offset:self._read_offset + read_size]
        self._read_offset += read_size
        return read_size

    def write(self, b):
        self._write_data[self._write_offset:self._write_offset + len(b)] = b
        self._
