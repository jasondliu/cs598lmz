import io
class File(io.RawIOBase):

    def __init__(self, file):
        self.file = file
        self.position = 0

    def read(self, size=None):
        if size is None:
            size = -1
        data = self.file.read(size)
        self.position += len(data)
        return data

    def write(self, b):
        self.file.write(b)
        self.position += len(b)
        return len(b)

    def tell(self):
        return self.position

    def seek(self, offset, whence=0):
        if whence == 0:
            n = offset
        elif whence == 1:
            n = self.position + offset
        elif whence == 2:
            n = self.size + offset
        else:
            raise ValueError("Invalid value for whence: %r" % (whence,))
        if n < 0:
            raise ValueError("Seek before start of file")
        self.position = n
        return n

    def seekable(self):
        return True

    def close(self
