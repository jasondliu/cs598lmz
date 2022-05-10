import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.file = open(path, mode)

    def read(self, size=-1):
        return self.file.read(size)

    def readable(self):
        return self.file.readable()

    def seekable(self):
        return self.file.seekable()

    def writable(self):
        return self.file.writable()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def write(self, b):
        return self.file.write(b)

    def readinto(self, b):
        return self.file.readinto(b)

    def close(self):
        return self.file.close()

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        return self.file.flush()

    def isatty(self):
        return self.file
