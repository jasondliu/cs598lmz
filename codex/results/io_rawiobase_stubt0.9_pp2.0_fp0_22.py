import io
class File(io.RawIOBase):
    
    def __init__(self, file, mode = 'r', block_size = io.DEFAULT_BUFFER_SIZE):
        self._file = open(file, mode + 'b')
        self._block_size = block_size
    
    
    def close(self):
        if self._file:
            self._file.close()
            self._file = None
    
    
    def readable(self):
        return True
    
    
    def readinto(self, b):
        return self._file.readinto(b)
    
    
    def read(self, size = -1):
        return self._file.read(size)
    
    
    def read1(self, size = -1):
        return self._file.read(min(size, self._block_size))
    
    
    def seekable(self):
        return True
    
    
    def seek(self, offset, whence = os.SEEK_SET):
        self._file.seek(offset, whence)
    
    
    def tell(self):
