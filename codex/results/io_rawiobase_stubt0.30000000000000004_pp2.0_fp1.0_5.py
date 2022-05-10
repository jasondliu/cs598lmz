import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fd = None
        self.open()

    def open(self):
        self.fd = os.open(self.filename, self.mode)

    def close(self):
        os.close(self.fd)

    def read(self, n=-1):
        return os.read(self.fd, n)

    def write(self, b):
        return os.write(self.fd, b)

    def seek(self, offset, whence=os.SEEK_SET):
        return os.lseek(self.fd, offset, whence)

    def tell(self):
        return os.lseek(self.fd, 0, os.SEEK_CUR)

f = File('/tmp/foo', os.O_RDWR)
f.write(b'hello world')
f.seek(0)
print(f.read())
f.close()
</code>

