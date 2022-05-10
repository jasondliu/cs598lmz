import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = open(self.path, self.mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readline(self, size=-1):
        return self.file.readline(size)
    def readlines(self, sizehint=-1):
        return self.file.readlines(sizehint)
    def write(self, b):
        return self.file.write(b)
    def writelines(self, lines):
        return self.file.writelines(lines)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        return self.file.flush()

