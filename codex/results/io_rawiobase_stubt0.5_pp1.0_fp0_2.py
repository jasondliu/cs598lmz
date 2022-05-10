import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode='r', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.file_name = file_name
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener

        self.file = open(file_name, mode, buffering, encoding, errors, newline, closefd, opener)
        self.file.seek(0, 2)
        self.size = self.file.tell()
        self.file.seek(0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def read(self, size=-1):
        return self.file.read(size)

    def readinto(self, b):
        return self.file
