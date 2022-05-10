import io
# Test io.RawIOBase
import io
import os
import sys
import unittest
import weakref
import _pyio as pyio

class MockRawIO(io.RawIOBase):
    def __init__(self, read_stack=()):
        self._read_stack = list(read_stack)
        self._write_stack = []
        self._reads = 0
        self._extraneous_reads = 0
        self._writes = 0
        self._extraneous_writes = 0
        self._seek_count = 0
        self._closed = False
        self._readinto_count = 0
        self._readinto_buffer = None
        self._readinto_result = None
        self._read1_count = 0
        self._read1_result = None

    def read(self, n=-1):
        self._reads += 1
        if self._read_stack:
            data = self._read_stack.pop(0)
            if isinstance(data, Exception):
                raise data
            return data
        self._extraneous_reads += 1
        return b
