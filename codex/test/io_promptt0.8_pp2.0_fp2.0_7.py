import io
# Test io.RawIOBase.flush() interleaved with .write()

class FlusherRawIO(io.RawIOBase):
    def __init__(self, bufsize):
        self.bufsize = bufsize
        self.buf = b''

    def close(self):
        pass

    def flush(self):
        self._write(b'', swallow_output=True)

    def read(self, size=-1):
        raise io.UnsupportedOperation

    def write(self, b):
        self._write(b)

    def _write(self, b, swallow_output=False):
        if b:
            print(b, end='')
            self.buf += b
            r = self.buf.rfind(b'\n', 0, self.bufsize)
            if r >= 0:
                self.buf = self.buf[r+1:]
        if not swallow_output:
            print('flush')

import unittest
