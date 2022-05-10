import io
# Test io.RawIOBase

from test import support
from test.support import bigmemtest, import_module

from io import RawIOBase
from io import SEEK_SET, SEEK_CUR, SEEK_END
from io import UnsupportedOperation, BlockingIOError

class CIOBase(RawIOBase):
    def __init__(self):
        self._read_stack = []
        self._write_stack = []
        self._seek_stack = []
        self._tell_stack = []

    def push(self, read_data, num_read, write_data, num_written, seek_pos,
             tell_pos):
        self._read_stack.append((read_data, num_read))
        self._write_stack.append((write_data, num_written))
        self._seek_stack.append(seek_pos)
        self._tell_stack.append(tell_pos)

    def pop(self):
        if len(self._read_stack) > 0:
            read_data, num_read = self._read_stack.pop(0)
        else
