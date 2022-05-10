import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.file_size = 0
        self.position = 0
        self.buffer = b''

    def open(self):
        self.file = open(self.file_name, self.mode)
        self.file_size = os.stat(self.file_name).st_size

    def close(self):
        self.file.close()

    def read(self, size=-1):
        if size == -1:
            size = self.file_size - self.position

        if self.position + size > self.file_size:
            size = self.file_size - self.position

        if size > len(self.buffer):
            self.buffer += self.file.read(size - len(self.buffer))

        data = self.buffer[:size]
        self.buffer = self.buffer[size:]
        self.position += size
        return data

    def readable(self
