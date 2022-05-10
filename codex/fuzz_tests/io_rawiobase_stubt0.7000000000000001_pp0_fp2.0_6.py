import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
        self.buffer = b""
        self.pos = 0
    
    def open(self):
        if self.fd is None:
            self.fd = open(self.path, "rb")
            self.buffer = b""
            self.pos = 0
    
    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
            self.buffer = b""
            self.pos = 0
    
    def _fill(self, size):
        if len(self.buffer) < size:
            self.buffer += self.fd.read(size - len(self.buffer))
    
    def _read(self, size):
        self._fill(size)
        data = self.buffer[:size]
        self.buffer = self.buffer[size:]
        self.pos += size
        return data
    
    def readable(self):
        return True
    
    def readinto(
