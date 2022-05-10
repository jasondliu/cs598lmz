import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class MyRawIO(_io.RawIOBase):
    def __init__(self, initial_bytes=b''):
        self.read_history = []
        self.write_history = []
        self.readinto_history = []
        self.read_history = []
        self.write_history = []
        self.readinto_history = []
        self.read_history = []
        self.write_history = []
        self.readinto_history = []
        self.seek_history = []
        self.tell_history = []
        self.closed = 0
        self.initial_bytes = initial_bytes
        self.bytes = initial_bytes

    def read(self, n=-1):
        self.read_history.append(n)
        if n < 0:
            result = self.bytes
            self.bytes = b''
        else:
            result = self.bytes[:n]
            self.bytes = self.bytes[n:]
        return result


