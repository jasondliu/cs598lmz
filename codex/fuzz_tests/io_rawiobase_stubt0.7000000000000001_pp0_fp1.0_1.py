import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def write(self, s):
        self.f.write(s)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)
    def seekable(self):
        return True
    def tell(self):
        return self.f.tell()
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        self.f.flush()
    def close(self):
        self.f.close()

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.error import ConnectionDone
import cStringIO

class AbstractBuffer(object):
    @classmethod
    def from_bytes(cls, bytes):
        return cls(cStringIO.StringIO(bytes))

   
