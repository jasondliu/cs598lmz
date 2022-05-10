import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'rb')
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
        return self.file.tell()
    def tell(self):
        return self.file.tell()
    def write(self, data):
        raise NotImplementedError()
    def writable(self):
        return False
    def writelines(self, lines):
        raise NotImplementedError()

class FileCache(object):
    def __init__(self, filename, maxsize=1024*1024):
        self.filename = filename
        self.maxsize = maxsize
        self.size = 0
        self.cache = []
        self.offset = 0
        self
