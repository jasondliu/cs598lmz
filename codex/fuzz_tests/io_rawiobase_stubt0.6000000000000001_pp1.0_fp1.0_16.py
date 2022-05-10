import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
        self.encoding = "utf-8"
    def close(self):
        if self.closed:
            return
        try:
            if self.writable():
                self.flush()
        finally:
            self.closed = True
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        if self.writable():
            self.file.flush()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return "r" in self.mode
    def readline(self, size=-1):
        return self.file.readline(size)
    def readlines(self, hint=-1):
        return self.file.readlines(hint)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def seekable(self):
       
