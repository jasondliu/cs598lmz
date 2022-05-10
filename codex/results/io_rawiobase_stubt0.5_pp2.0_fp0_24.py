import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fd = None
    def open(self):
        if self.fd is None:
            self.fd = os.open(self.filename, os.O_RDONLY)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self.fd, b)
    def read(self, n=-1):
        buf = bytearray(n)
        n = self.readinto(buf)
        return buf[:n]

with File('/dev/tty', 'r') as f:
    print(f.read())

# 同样，你
