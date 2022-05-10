import io
# Test io.RawIOBase for read/write
class BytesIOWrapper(io.RawIOBase):
    def __init__(self, buffer):
        self.buffer = buffer
        self.position = 0

    def readinto(self, b):
        data_to_read = min(len(self.buffer) - self.position, len(b))
        if data_to_read == 0:
            return 0

        b[:data_to_read] = self.buffer[self.position:self.position + data_to_read]
        self.position += data_to_read
        return data_to_read

    def write(self, b):
        data_to_write = len(b)
        self.buffer[self.position:self.position + data_to_write] = b
        self.position += data_to_write
        return data_to_write

    def read(self, n=-1):
        if n < 0:
            n = len(self.buffer) - self.position
        data = self.buffer[self.position:self.position + n]
