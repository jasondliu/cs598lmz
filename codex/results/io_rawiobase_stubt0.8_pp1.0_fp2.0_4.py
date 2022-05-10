import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="r", encoding="utf8"):
        super().__init__()
        self._file = open(filename, mode)
        self.encoding = encoding
        self.errors = "strict"
    
    def close(self):
        self._file.close()
    
    @property
    def closed(self):
        return self._file.closed
    
    @property
    def name(self):
        return self._file.name
    
    def fileno(self):
        return self._file.fileno()
    
    def flush(self):
        pass
    
    def isatty(self):
        return False
    
    def readable(self):
        return False
    
    def readline(self, size=-1):
        if size < 0:
            line = self._file.readline()
        else:
            line = self._file.readline(size)
        return line.decode(self.encoding, self.errors)
    
    def readlines(self, hint=-
