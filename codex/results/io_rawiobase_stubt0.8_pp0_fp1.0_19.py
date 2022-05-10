import io
class File(io.RawIOBase):
    FILE_MODES = ('r', 'r+', 'w', 'w+', 'a', 'a+')

    def __init__(self, file, mode='r'):
        if mode not in self.FILE_MODES:
            raise ValueError('Invalid file mode: {}'.format(mode))
        
        self._mode = mode
        self._file = file

    def close(self):
        if self.closed:
            return
        self._file.close()
        
    @property
    def closed(self):
        return self._file.closed

    @property
    def name(self):
        return self._file.name
    
    def readable(self):
        return self._mode in ('r', 'r+', 'a+')
    
    def readinto(self, b):
        return self._file.readinto(b)
    
    def readline(self, limit=-1):
        return self._file.readline(limit)
    
    def readlines(self, hint=-1):
        return self._file.readlines(h
