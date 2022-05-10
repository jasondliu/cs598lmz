import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.closed = False
        self.f = open(filename, mode)
    def close(self):
        self.f.close()
        self.closed = True
    def fileno(self):
        return self.f.fileno()
    def seek(self, offset, whence):
        self.f.seek(offset, whence)
    def readable(self):
        return self.mode in ('r', 'rb')
    def writable(self):
        return self.mode in ('w', 'wb')
    def readinto(self, b):
        return self.f.readinto(b)
    def write(self, b):
        return self.f.write(b)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
    def __del__(self):
        if not self.closed:
           
