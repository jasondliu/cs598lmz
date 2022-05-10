import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self._fd = os.open(filename, os.O_RDONLY)
        self.buffer = b""
        self.buffer_size = 10
        self.buffer_pos = 0
        self.buffer = os.read(self._fd, self.buffer_size)
    def readable(self):
        return True
    def readinto(self, b):
        if not self.buffer:
            return None
        n = len(b)
        view = memoryview(b)
        while len(view) and self.buffer:
            nread = os.readv(self._fd, [view[:self.buffer_size]])
            self.buffer_pos += nread
            view = view[nread:]
        return n
    def seek(self, pos, whence=os.SEEK_SET):
        if whence == os.SEEK_CUR:
            pos += self.buffer_pos
        elif whence == os.SEEK_END:
            st = os.fstat(self._fd)
            pos
