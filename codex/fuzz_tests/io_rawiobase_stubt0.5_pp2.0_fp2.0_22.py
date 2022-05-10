import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = os.open(path, os.O_RDONLY)
        self.size = os.path.getsize(path)
        self.tell = 0
    def read(self, size=-1):
        if size < 0:
            size = self.size - self.tell
        if size == 0:
            return b""
        os.lseek(self.fd, self.tell, os.SEEK_SET)
        data = os.read(self.fd, size)
        self.tell += len(data)
        return data
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.tell = offset
        elif whence == os.SEEK_CUR:
            self.tell += offset
        elif whence == os.SEEK_END:
            self.tell = self.size + offset
