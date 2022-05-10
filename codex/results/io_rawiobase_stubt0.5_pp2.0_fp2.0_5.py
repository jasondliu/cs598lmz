import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1):
        self.name = name
        self.mode = mode
        self.file = self._open(name, mode, buffering)
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()
    
    def __repr__(self):
        return '<open file \'%s\', mode \'%s\'>' % (self.name, self.mode)
    
    def _open(self, name, mode, buffering):
        return open(name, mode, buffering)
    
    def close(self):
        if self.file is not None:
            try:
                self.file.close()
            finally:
                self.file = None
    
    def fileno(self):
        return self.file.fileno()
    
    def flush(self):
        return self.file.flush()
    
    def isatty(self):
        return self.
