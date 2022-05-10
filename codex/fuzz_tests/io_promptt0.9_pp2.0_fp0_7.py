import io
# Test io.RawIOBase.readinto()
import weakref

from test import support


class MockRawIO(io.RawIOBase):
    """Base class to build mock raw I/O objects from.

    The only overridden method is readinto(), which generates a bytearray
    object of requested length, filled with consecutive numbers.
    """

    def __init__(self, read_stack=()):
        """Constructor.

        Optional argument read_stack is a sequence of integers — lengths
        of byte strings that should be returned by successive calls to
        read().
        """
        self.read_stack = read_stack
        self._read_stack_view = memoryview(read_stack)
        self._read_stack_pos = 0
        self.readinto_calls = 0
        self.readinto_num_args = None
        self.closed = 0

    def close(self):
        self.closed = 1

    def readinto(self, b):
        self.readinto_calls += 1
        len_readstack = len(self.read_stack)
        if self._read
