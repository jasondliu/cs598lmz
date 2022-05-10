import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def read(self, n=-1):
        self.file.seek(self.offset)
        s = self.file.read(n)
        self.offset = self.file.tell()
        return s
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.file.seek(0, 2) + offset
    def tell(self):
        return self.offset
    def readable(self):
        return True
    def writable(self):
        return False
    def flush(self):
        pass
    def close(self):
        pass

def get_file_object(file):
    if isinstance(file, io.RawIOBase):
        return file
    elif isinstance(file, str):
        return open
