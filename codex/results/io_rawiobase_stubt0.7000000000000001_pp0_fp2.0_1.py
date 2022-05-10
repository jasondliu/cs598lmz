import io
class File(io.RawIOBase):
    def __init__(self, path, mode='rb'):
        self.path = path
        self.mode = mode
        self.size = os.stat(self.path).st_size
        self.fp = open(self.path, self.mode)
        self.pos = 0
 
    def __repr__(self):
        return '<File {!r}>'.format(self.path)
 
    def readable(self):
        return self.mode in ('r', 'rb', 'r+', 'rb+', 'w+', 'wb+')
 
    def writable(self):
        return self.mode in ('w', 'wb', 'r+', 'rb+', 'w+', 'wb+')
 
    def seekable(self):
        return True
 
    def read(self, n=-1):
        self.fp.seek(self.pos)
        data = self.fp.read(n)
        self.pos = self.fp.tell()
        return data
 
    def read1(self, n=-
