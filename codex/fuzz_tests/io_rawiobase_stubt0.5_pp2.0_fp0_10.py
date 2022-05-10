import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_WRONLY | os.O_CREAT)
    def write(self, b):
        os.write(self.fd, b)
    def close(self):
        os.close(self.fd)

with open('/tmp/junk.data', 'wb') as f:
    f.write(b'Hello World\n')

f = File('/tmp/junk.data')
f.write(b'Hello World\n')
f.close()

class File2(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_WRONLY | os.O_CREAT)
    def write(self, b):
        os.write(self.fd, b)
    def close(self):
        os.close(self.fd)
    def fileno(self):
        return self.fd

