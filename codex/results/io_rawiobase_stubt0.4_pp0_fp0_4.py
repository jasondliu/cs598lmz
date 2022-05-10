import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    def seekable(self):
        return self.file.seekable()
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def readable(self):
        return self.mode in ('r', '+', 'a+', 'r+')
    def writable(self):
        return self.mode in ('w', 'w+', 'a', 'a+', 'r+')
    def __repr__(self):
        return '<File {!r}>'.format(self.file)

class BytesIO(io.BytesIO):
   
