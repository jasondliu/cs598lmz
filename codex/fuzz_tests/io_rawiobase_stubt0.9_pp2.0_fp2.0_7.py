import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.isdir = False
        self._file = open(filename, mode)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self.closed:
            pass
        elif not self.isdir:
            self._file.close()
        self.__dict__.clear()

    def readable(self):
        return self._file.readable
    
    def read(self, *args, **kwargs):
        return self._file.read(*args, **kwargs)
    
    def readline(self, *args, **kwargs):
        return self._file.readline(*args, **kwargs)
    
    def readlines(self, *args, **kwargs):
        return self._file.readlines(*args, **kwargs)
    
    def writeable(self):
        return self._file.writeable
    
    def write
