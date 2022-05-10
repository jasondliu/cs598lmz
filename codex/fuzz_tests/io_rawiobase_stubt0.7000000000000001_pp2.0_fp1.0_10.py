import io
class File(io.RawIOBase):
    def fileno(self):
        return self.fd
        # return os.open(path, os.O_RDONLY | os.O_BINARY)
    def open(self, path):
        self.fd = os.open(path, os.O_RDONLY | os.O_BINARY)
        return self.fd
def read_bytes(self, n):
    return os.read(self.fd, n)

def read_file(path):
    file = File()
    file.open(path)
    buf = file.read(1024)
    file.close()
    return buf
</code>

