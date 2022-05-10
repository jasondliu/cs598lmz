import io
# Test io.RawIOBase

from test import support
import unittest
from unittest import mock


class MockRawIO(io.RawIOBase):
    # Can be used to mock out io.BufferedIOBase.
    #
    # The implementation here is robust, but not very efficient.
    def __init__(self, read_results, readinto_results=None, seek_value=0,
                 sample_size=4096):
        self._read_results = iter(read_results)
        self._readinto_results = iter(readinto_results or read_results)
        self.readinto1_calls = 0
        self.read1_calls = 0
        self.seek_value = seek_value
        self.tell_values = itertools.cycle(range(seek_value + 2))
        self.sample_size = sample_size

    def readinto1(self, r):
        next_readinto1_result = next(self._readinto_results)
        self.readinto1_calls += 1
        length = min(len(next_readinto1
