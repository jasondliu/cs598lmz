import io
# Test io.RawIOBase
import socket
import _io
import io
import os
import sys
import time
import traceback
import unittest


class MockRawIO(io.RawIOBase):

    def __init__(self, read_data):
        self.read_data = read_data
        self.read_index = 0
        self.read_delimiter = b''
        self.read_reached_eof = False

    def readinto(self, b):
        if self.read_index >= len(self.read_data):
            return 0

        data = self.read_data[self.read_index:]
        if self.read_delimiter:
            delimiter_index = data.index(self.read_delimiter)
            data = data[:delimiter_index + len(self.read_delimiter)]

        n = len(b)
        if len(data) > n:
            data = data[:n]
        b[:len(data)] = data
        self.read_index += len(data)

