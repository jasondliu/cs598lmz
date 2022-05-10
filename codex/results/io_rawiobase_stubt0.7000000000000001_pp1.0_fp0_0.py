import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
    
    def flush(self):
        if self.fd:
            os.fsync(self.fd)
    
    def close(self):
        if self.fd:
            os.close(self.fd)
            self.fd = None
    
    def __enter__(self):
        self.fd = os.open(self.path, os.O_RDONLY)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def readinto(self, b):
        return os.readv(self.fd, [memoryview(b)])

with File(path) as f:
    print(f.read(2))
    print(f.read(2))

print(f.readinto(bytearray(b'abc')))

print(f.closed, f.readable(), f.seekable())

try:
    f
