import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.fd = None
        self.buffer = None
        self.buffer_pos = 0
        self.buffer_size = 0
        self.buffer_dirty = False
        self.buffer_end = False
        self.buffer_size = 4096
        self.buffer_pos = 0
        self.buffer_dirty = False
        self.buffer_end = False
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    def close(self):
        if self.fd is not None:
            self.flush()
            os.close(self.fd)
            self.fd = None
    def flush(self):
        if self.buffer_dirty:
            os.lseek(self.fd, self.buffer_pos, io.SEEK_SET)
            os.write(self.fd, self.buffer)
            self.buffer_dirty = False

