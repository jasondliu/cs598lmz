import io
# Test io.RawIOBase support
import random

class MyRawIO(io.RawIOBase):
    def readinto(self, buf):
        """Read up to len(b) bytes into b, and return the number of bytes read.

        If the object is in non-blocking mode and no bytes are available,
        None is returned.
        """
        for i in range(len(buf)):
            rand = random.randint(0, 0xFFFF)
            buf[i] = rand & 0xFF
        return len(buf)

# Test io.BufferedIOBase support
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self):
        self.raw = MyRawIO()
        self._read_buf = bytearray()
        self._write_buf = bytearray()
        self._read_buf_size = self._write_buf_size = 10

    def read(self, sz):
        if not self._read_buf:
            self._read_buf.extend(self.raw.read(self._read_buf_size))
