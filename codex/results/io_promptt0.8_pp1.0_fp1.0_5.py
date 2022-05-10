import io
# Test io.RawIOBase

io.RawIOBase.readinto(b"")
io.RawIOBase.readinto1(b"")

from io import RawIOBase
# Test io.RawIOBase

RawIOBase.readinto(b"")
RawIOBase.readinto1(b"")

from io import RawIOBase
from io import BufferedIOBase
from io import IOBase
from io import TextIOBase
from io import BytesIO
from io import StringIO

class MyRawIO(RawIOBase):
    def fileno(self):
        return None
    def write(self, data):
        return None
    def readinto(self, data):
        return None

class MyBufferedIO(BufferedIOBase):
    def fileno(self):
        return None
    def write(self, data):
        return None
    def read(self, data):
        return None

class MyIO(IOBase):
    def fileno(self):
        return None
    def write(self, data):
        return None
    def read(self, data):
