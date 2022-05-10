import io
class File(io.RawIOBase):
    '''
    this is a file interface,
    that stores data into memory
    '''
    def __init__(self, content = bytes()):
        self.content = content
        self.location = 0
    
    def close(self):
        super().close()
        self.content = bytes()
        self.location = 0
    
    def seek(self, pos, whence = io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.location = pos
            return True
        elif whence == io.SEEK_CUR:
            self.location += pos
            return True
        elif whence == io.SEEK_END:
            self.location = len(self.content) + pos
            return True
        else:
            raise ValueError()

    def read(self, size = -1):
        if len(self.content) < self.location:
            return bytes()

        if size == -1 or len(self.content) - self.location < size:
            result = self.content[self.location:]
           
