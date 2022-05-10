import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)
        self.encoding = 'utf-8'
        self.mode = mode
    def close(self):
        self.file.close()
    def readable(self):
        return 'r' in self.mode
    def seekable(self):
        return True
    def writable(self):
        return 'w' in self.mode
    def read(self, size=-1):
        return self.file.read(size)
    def seek(self, pos, whence=0):
        self.file.seek(pos, whence)
    def write(self, data):
        return self.file.write(data)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

class FileManager():
    def __init__(self):
        self.files = {}
    def __enter__(self):
        return self
    def __exit__(self, *args):
       
