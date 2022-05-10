import io
# Test io.RawIOBase.readinto()
import random
import time
import array
try:
    buffer
except NameError:
    buffer = memoryview

class SimpleWriter(io.RawIOBase):

    def __init__(self, target):
        self._target = memoryview(target)
        self._target_write_offset = 0

    def write(self, b):
        b = memoryview(b).cast('B')
        self._target.cast('B')[self._target_write_offset : self._target_write_offset + len(b)] = b
        self._target_write_offset += len(b)

    def tell(self):
        return self._target_write_offset

    def close(self):
        pass


class SimpleReader(io.RawIOBase):

    def __init__(self, source):
        self._source = memoryview(source)
        self._source_read_offset = 0

