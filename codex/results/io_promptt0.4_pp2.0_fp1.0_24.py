import io
# Test io.RawIOBase

import _io
import unittest
from test import support
from test.support import bigmemtest

# RawIOBase is an abstract base class.  The following class is used
# for testing.

class TestRawIO(io.RawIOBase):

    def __init__(self, test_dict):
        self._read_stack = []
        self._write_stack = []
        self._reads = test_dict.get('reads', [])
        self._writes = test_dict.get('writes', [])
        self._seek = test_dict.get('seek', None)
        self._readinto = test_dict.get('readinto', None)
        self._readinto1 = test_dict.get('readinto1', None)
        self._readall = test_dict.get('readall', None)
        self._read1 = test_dict.get('read1', None)
        self._extraneous_reads = test_dict.get('extraneous_reads', [])
        self._extraneous_reads_ok = test_dict.
