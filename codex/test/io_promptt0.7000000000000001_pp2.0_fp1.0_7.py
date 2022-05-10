import io
# Test io.RawIOBase.readinto()

import io
from _io import DEFAULT_BUFFER_SIZE

# Test a concrete implementation

class MyIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def readinto(self, b):
        sz = len(self.data) - self.pos
        if sz == 0:
            return 0
        b[0:sz] = self.data[self.pos:]
        self.pos += sz
        return sz

    def writable(self):
        return False

# Test the abstract base class

for methname, func in vars(io.RawIOBase).items():
    if methname.startswith('_'):
        continue
    if hasattr(MyIO, methname):
        continue
    raise AssertionError('abstract method %s() not defined' % methname)

buf = bytearray(DEFAULT_BUFFER_SIZE)
