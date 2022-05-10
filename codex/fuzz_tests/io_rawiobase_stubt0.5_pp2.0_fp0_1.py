import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.close()

    def close(self):
        if self.fd is not None:
            if self.closefd:
                os.close(self.fd)
        self.fd = None

    def fileno(self):
        if self.fd is None:
            if self.opener is not None:
                self.fd = self.opener(self.name, self.mode)
            else:
                self.fd = os.open(self.name, self.mode)
        return self.fd

    def __del__(self):
        self.close()

class FileIO(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.close
