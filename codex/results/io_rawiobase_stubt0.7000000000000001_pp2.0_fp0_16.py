import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file

    def read(self, n=-1):
        return self.file.read(n)

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        if self.file != sys.stdin:
            self.file.close()
        self.file = None

    def flush(self):
        pass

class FileInput(File):
    def readline(self, size=-1):
        return self.file.readline(size)

    def readlines(self, hint=-1):
        return self.file.readlines(hint)

    def __iter__(self):
        return iter(self.file)

class FileOutput(File):
    def write(self, s
