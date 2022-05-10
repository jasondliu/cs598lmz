import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.f = open(path, mode)
        self.mode = mode
    def read(self, size=-1):
        return self.f.read(size)
    def readinto(self, b):
        return self.f.readinto(b)
    def write(self, b):
        return self.f.write(b)
    def fileno(self):
        return self.f.fileno()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def __del__(self):
        if self.mode == 'w':
            self.f.close()

with File('test.txt', 'w') as f:
    f.write('hello')

with File('test.txt', 'r') as f:
    print
