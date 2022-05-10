import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r", *args, **kwargs):
        self.path = path
        self.mode = mode
        self.file = io.open(path, mode, *args, **kwargs)
        if 'b' in mode:
            self.read = self.read_binary
            self.write = self.write_binary
        else:
            self.read = self.read_text
            self.write = self.write_text
    
    def read_text(self, size=-1):
        return self.file.read(size)
    
    def write_text(self, s):
        return self.file.write(s)
    
    def read_binary(self, size=-1):
        return self.file.read(size)
    
    def write_binary(self, s):
        return self.file.write(s)
    
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    
    def tell(self):
        return self.
