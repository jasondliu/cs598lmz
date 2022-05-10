import io
# Test io.RawIOBase by using an in-memory buffer as a raw I/O implementation.

import io
import sys

# A buffer that reads from a list of buffers.
class MultiBuffer(io.RawIOBase):

    def __init__(self, buffers):
        self.buffers = buffers

    def readable(self):
        return True

    def readinto(self, b):
        if not self.buffers:
            return 0
        n = len(self.buffers[0])
        if len(b) < n:
            n = len(b)
        b[:n] = self.buffers[0][:n]
        if n < len(self.buffers[0]):
            self.buffers[0] = self.buffers[0][n:]
        else:
            del self.buffers[0]
        return n

# A buffer that writes into a list of buffers.
class MultiBufferIO(io.RawIOBase):

    def __init__(self, buffers):
        self.buffers = buffers

    def writable(self):
        return
