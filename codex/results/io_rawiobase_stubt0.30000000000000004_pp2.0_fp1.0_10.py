import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
        self.closed = False
    def read(self, n=-1):
        if n >= 0:
            self.seek(n, 1)
            return self.file.read(n)
        else:
            return self.file.read()
    def seek(self, offset, whence=0):
        if whence == 1:
            offset += self.offset
        elif whence == 2:
            offset += self.file.size
        self.offset = offset
        return self.file.seek(offset)
    def tell(self):
        return self.offset
    def close(self):
        self.closed = True
        return self.file.close()
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True

class FileSystem(object):
    def __init__(self, root):
        self.root = root
    def open(self, path, mode='rb'
