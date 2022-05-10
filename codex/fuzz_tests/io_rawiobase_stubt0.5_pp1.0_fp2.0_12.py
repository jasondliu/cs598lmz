import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def close(self):
        if self.file:
            self.file.close()

    def isatty(self):
        return False

    def readable(self):
        return self.mode == 'r'

    def readline(self, size=-1):
        return self.file.readline(size)

    def readlines(self, size=-1):
        return self.file.readlines(size)

    def seekable(self):
        return self.file.seekable()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def writable(self):
        return self.mode == 'w'

    def write(self, b):
        return self.file.write(b)

    def writelines(self, lines):
        return self.file.writelines
