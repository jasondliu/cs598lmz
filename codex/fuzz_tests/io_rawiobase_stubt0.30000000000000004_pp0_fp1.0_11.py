import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self._file = None
    def open(self):
        self._file = open(self.name, self.mode)
    def close(self):
        self._file.close()
    def read(self, size=-1):
        return self._file.read(size)
    def write(self, b):
        return self._file.write(b)
    def flush(self):
        return self._file.flush()
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def fileno(self):
        return self._file.fileno()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def __del__(self):
        self.close()

