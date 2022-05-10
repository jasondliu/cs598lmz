import io
# Test io.RawIOBase.readinto
import io
import os
import array
import unittest
import tempfile
try:
    import threading
except ImportError:
    threading = None

class ByteBuffer(io.RawIOBase):
    def __init__(self, initial_bytes=b''):
        self.read_buffer = array.array('B', initial_bytes)
        self.read_buffer_offset = 0

    def readable(self):
        return True

    def readinto(self, b):
        num_bytes = len(self.read_buffer) - self.read_buffer_offset
        if num_bytes == 0:
            return None
        if len(b) < num_bytes:
            num_bytes = len(b)
        b[:num_bytes] = self.read_buffer[self.read_buffer_offset:
                                        self.read_buffer_offset + num_bytes]
        self.read_buffer_offset += num_bytes
        return num_bytes

    def write(self, b):
        self.read_buffer.frombytes(b)
