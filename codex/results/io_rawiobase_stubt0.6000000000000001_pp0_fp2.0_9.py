import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.fd = open(filename, "rb")
    def read(self, size=-1):
        return self.fd.read(size)
    def readable(self):
        return True

data = File("/dev/urandom").read(100)
</code>

