import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.mode = mode
        self.name = name
        self.file = None
        if mode.find('w') >= 0:
            self.file = open(name, mode)
        elif mode.find('r') >= 0:
            self.file = open(name, mode)
        else:
            raise ValueError('Unsupported mode: ' + mode)
    def close(self):
        self.file.close()
        return
    def readable(self):
        return self.mode.find('r') >= 0
    def writable(self):
        return self.mode.find('w') >= 0
    def seekable(self):
        return self.mode.find('r') >= 0
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def read(self, size=-1):
       
