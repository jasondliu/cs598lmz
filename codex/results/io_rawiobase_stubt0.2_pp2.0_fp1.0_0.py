import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.file_name, self.mode)

    def close(self):
        self.file.close()

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def flush(self):
        return self.file.flush()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def readable(self):
        return self.file.readable()

    def writable(self):
        return
