import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.data = list()
        self.file = None
        self.pos = 0
        
    def _load(self):
        if self.file is None:
            self.file = open(self.path, 'rb')
            self.data = self.file.read()
        
    def read(self, size=-1):
        self._load()
        if size < 0:
            size = len(self.data) - self.pos
        data = self.data[self.pos:self.pos+size]
        self.pos += size
        return data
    
    def seek(self, offset, whence=io.SEEK_SET):
        self._load()
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END:
            self.pos = len(self.data) + offset
        else:
            raise Value
