import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.mode = mode
        self.name = name
        self.file = None
        self.buffer = bytearray(0)
        self.offset = 0
        self.closed = False
        if self.mode in ('r', 'a'):
            self.file = open(self.name, 'rb')
            self.buffer = bytearray(self.file.read())
        elif self.mode in ('w', 'rw'):
            self.file = open(self.name, 'wb')

    def read(self, size=-1):
        if size == -1:
            size = len(self.buffer) - self.offset
        data = self.buffer[self.offset:self.offset + size]
        self.offset += size
        return bytes(data)

    def readall(self):
        return self.buffer[self.offset:]

    def write(self, data):
        if self.mode in ('r', 'a'):
            raise io.UnsupportedOperation('
