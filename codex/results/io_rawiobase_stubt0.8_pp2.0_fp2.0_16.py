import io
class File(io.RawIOBase):
    def __init__(self, file, mode="rb", closefd=True):
        os.stat_float_times(False)
        self.file = open(file, mode=mode, closefd=closefd)
    def readinto(self, b):
        return self.file.readinto(b)
    def write(self, b):
        return self.file.write(b)
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        return self.file.close()
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        return self.file.flush()
    def isatty(self):
        return self.file.isat
