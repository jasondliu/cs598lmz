import io
class File(io.RawIOBase):
    def __init__(self, path, mode, *args, **kwargs):
        self.path = path
        self.mode = mode
        self.file = open(path, mode, *args, **kwargs)
        self.buffer = b''
        self.buffer_pos = 0
        self.buffer_size = 0
        self.closed = False

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def read(self, size=-1):
        if self.buffer_size == 0:
            return self.file.read(size)
        if size < 0:
            new_data = self.buffer[self.buffer_pos:] + self.file.read()
            self.buffer_pos = 0
            self.buffer_size = 0
            return new_data
        if size <= self.buffer_size:
            new_data = self.buffer[self.buffer_pos:self.buffer_pos + size]
            self.buffer_pos += size
            self.buffer_size -= size
            return new
