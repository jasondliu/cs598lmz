import io
# Test io.RawIOBase.readinto()

# io.RawIOBase.readinto() is not implemented by io.FileIO.

# Note: The io module is not supported by Python 3.x, so this test
# is skipped on those platforms.

import sys
if sys.version_info >= (3, 0):
    print("io.RawIOBase.readinto() is not implemented by io.FileIO in Python 3.x")
    raise SystemExit

import os
import tempfile

class FileIO(io.RawIOBase):
    def __init__(self, mode):
        self.f = open(tempfile.mktemp(), mode)

    def close(self):
        self.f.close()

    def readable(self):
        return 'r' in self.f.mode

    def writable(self):
        return 'w' in self.f.mode

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.
