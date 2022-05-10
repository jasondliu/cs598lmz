import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.fd = None
        self.open()

    def open(self):
        self.fd = os.open(self.path, self.mode)

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def fileno(self):
        return self.fd

    def readinto(self, b):
        return os.read(self.fd, b)

    def write(self, b):
        return os.write(self.fd, b)

f = File('/tmp/test.txt', os.O_RDWR | os.O_CREAT)
f.write(b'Hello World')
f.close()

f = File('/tmp/test.txt', os.O_RDONLY)
print(f.read())
f.close()

f = File('/tmp/test.txt', os.O_RDWR | os.O
