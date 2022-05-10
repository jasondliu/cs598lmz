import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None

    def open(self):
        self.fd = os.open(self.name, self.mode)

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def fileno(self):
        if self.fd is None:
            self.open()
        return self.fd

    def __del__(self):
        self.close()

class FileWrapper:
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def __getattr__(self, name):
        return getattr(self.file, name)

    def read(self, size=-1):
        if size == -1:
            data = self.file.read()
        else:
            data = self.file.read(size)
       
