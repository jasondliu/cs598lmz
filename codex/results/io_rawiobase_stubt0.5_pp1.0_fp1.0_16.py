import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.file_name = file_name
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.close()
        self.open(file_name, mode, buffering, encoding, errors, newline, closefd, opener)

    def open(self, file_name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
